#!/usr/bin/env python3
"""Skill Tiento - CLI ejecutable.

Adaptado del plugin ChatGPT "tiento" (github.com/LucioB16/chatgpt-plugins).
Provee listado de sub-skills, construccion de breves y esqueleto de
generacion de imagenes IA.

Uso:
    python tiento.py --list
    python tiento.py --validate
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from typing import Dict, List, Optional

# Directorio que contiene este archivo (permite ejecutarlo desde cualquier cwd).
HERE = __import__("os").path.dirname(__import__("os").path.abspath(__file__))

SUB_SKILLS: Dict[str, str] = {
    "art-director": "Direccion de arte y concepto visual.",
    "interface-director": "Disenio de interfaz y mockups.",
    "visual-critic": "Critica visual de mockups.",
}

VALID_SKILLS = tuple(SUB_SKILLS.keys())


@dataclass
class Brief:
    """Breve de direccion de arte para un sub-skill."""

    skill: str
    subject: str
    audience: Optional[str] = None
    medium: Optional[str] = None
    aspect_ratio: Optional[str] = None
    exclusions: List[str] = field(default_factory=list)
    references: List[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "skill": self.skill,
            "subject": self.subject,
            "audience": self.audience,
            "medium": self.medium,
            "aspect_ratio": self.aspect_ratio,
            "exclusions": list(self.exclusions),
            "references": list(self.references),
        }

    def to_json(self, **kwargs) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, **kwargs)


class UnknownSkillError(ValueError):
    """Se lanza cuando el skill solicitado no existe."""


def list_skills() -> Dict[str, str]:
    """Devuelve los sub-skills disponibles mapeados a su descripcion."""
    return dict(SUB_SKILLS)


def build_brief(
    skill: str,
    subject: str,
    audience: Optional[str] = None,
    medium: Optional[str] = None,
    aspect_ratio: Optional[str] = None,
    exclusions: Optional[List[str]] = None,
    references: Optional[List[str]] = None,
) -> Brief:
    """Construye un Brief para el skill dado, validando que exista."""
    if skill not in VALID_SKILLS:
        raise UnknownSkillError(
            "Skill desconocido '%s'. Skills validos: %s" % (skill, ", ".join(VALID_SKILLS))
        )
    return Brief(
        skill=skill,
        subject=subject,
        audience=audience,
        medium=medium,
        aspect_ratio=aspect_ratio,
        exclusions=list(exclusions or []),
        references=list(references or []),
    )


def generate_image(brief: Brief) -> str:
    """Esqueleto de generacion de imagen.

    Por ahora no renderiza realmente: devuelve un mensaje indicando que el
    sub-skill es un esqueleto pendiente de implementar.
    """
    return (
        "Esqueleto: generacion de imagen para el skill '%s' aun no implementada. "
        "Sujeto: %s" % (brief.skill, brief.subject)
    )


def cmd_list() -> int:
    for skill, desc in SUB_SKILLS.items():
        print("%s - %s" % (skill, desc))
    return 0


def cmd_validate() -> int:
    """Valida que los sub-skills definidos sean consistentes."""
    skills = list_skills()
    if set(skills.keys()) != set(VALID_SKILLS):
        print("ERROR: inconsistencia entre SUB_SKILLS y VALID_SKILLS", file=sys.stderr)
        return 1
    for skill in VALID_SKILLS:
        brief = build_brief(skill=skill, subject="validacion de " + skill)
        assert brief.skill == skill
        assert brief.subject
    print("OK: %d sub-skills validos" % len(VALID_SKILLS))
    return 0


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(
        prog="tiento.py",
        description="Skill Tiento - direccion de arte para imagenes IA (esqueleto).",
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--list", action="store_true", help="Lista los sub-skills disponibles")
    group.add_argument("--validate", action="store_true", help="Valida los sub-skills definidos")
    args = parser.parse_args(argv)

    if args.list:
        return cmd_list()
    if args.validate:
        return cmd_validate()
    return 0


if __name__ == "__main__":
    sys.exit(main())
