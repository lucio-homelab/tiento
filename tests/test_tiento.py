#!/usr/bin/env python3
"""Tests del skill Tiento.

4 tests que cubren: listado de skills, construccion de breve valido,
rechazo de skill invalido y serializacion JSON del breve.
"""

import json
import sys

# Permite ejecutar los tests desde cualquier directorio.
sys.path.insert(0, __import__("os").path.dirname(__import__("os").path.abspath(__file__)) + "/..")

from tiento import Brief, UnknownSkillError, build_brief, generate_image, list_skills


def test_list_skills_returns_three_skills() -> None:
    skills = list_skills()
    assert set(skills) == {"art-director", "interface-director", "visual-critic"}
    assert all(isinstance(desc, str) and desc for desc in skills.values())
    print("OK test_list_skills_returns_three_skills")


def test_build_brief_valid_skill() -> None:
    brief = build_brief(
        skill="art-director",
        subject="Ilustracion de portada para LinkedIn",
        audience="profesionales",
        medium="digital",
        aspect_ratio="1:1",
    )
    assert brief.skill == "art-director"
    assert brief.subject == "Ilustracion de portada para LinkedIn"
    assert brief.exclusions == []
    assert brief.references == []
    print("OK test_build_brief_valid_skill")


def test_build_brief_invalid_skill_raises() -> None:
    try:
        build_brief(skill="no-existe", subject="x")
    except UnknownSkillError as exc:
        assert "no-existe" in str(exc)
        assert "art-director" in str(exc)
    else:
        raise SystemExit("FALLO: no se lanzo UnknownSkillError")
    print("OK test_build_brief_invalid_skill_raises")


def test_brief_to_dict_is_json_serializable() -> None:
    brief = build_brief(
        skill="interface-director",
        subject="Mockup de dashboard",
        exclusions=["gradientes genericos", "brillo innecesario"],
        references=["pantalla-referencia.png"],
    )
    data = json.dumps(brief.to_dict(), ensure_ascii=False)
    parsed = json.loads(data)
    assert parsed["skill"] == "interface-director"
    assert parsed["exclusions"] == ["gradientes genericos", "brillo innecesario"]
    print("OK test_brief_to_dict_is_json_serializable")


if __name__ == "__main__":
    test_list_skills_returns_three_skills()
    test_build_brief_valid_skill()
    test_build_brief_invalid_skill_raises()
    test_brief_to_dict_is_json_serializable()
    print("\nTODAS LAS PRUEBAS PASARON (4/4)")