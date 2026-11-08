---
name: tiento
version: 0.1.0
description: Skill de Hermes adaptado del plugin ChatGPT "tiento" para generación de imágenes IA. Provee breves de dirección de arte y esqueleto de generación de imagen.
author: LucioB16
origin: https://github.com/LucioB16/chatgpt-plugins (carpeta tiento/)
license: MIT
sub_skills:
  - art-director
  - interface-director
  - visual-critic
cli:
  commands:
    - name: --list
      description: Lista los sub-skills disponibles
    - name: --validate
      description: Valida un breve de habilidad
---

# Skill Tiento

Skill de Hermes para apoyar la generación de imágenes IA con dirección visual clara, adaptado del plugin ChatGPT `tiento` del repositorio [`github.com/LucioB16/chatgpt-plugins`](https://github.com/LucioB16/chatgpt-plugins).

Este es un **esqueleto**: define la estructura de breves (art-director, interface-director, visual-critic) y un punto de extensión `generate_image` que, por ahora, devuelve un mensaje de esqueleto sin renderizar realmente.

## Sub-skills

- `art-director/` — dirección de arte y concepto visual.
- `interface-director/` — diseño de interfaz y mockups.
- `visual-critic/` — crítica visual de mockups.

## Uso desde CLI

```
python tiento.py --list
python tiento.py --validate
```

## Uso desde Python

```python
from tiento import list_skills, build_brief, generate_image

skills = list_skills()
brief = build_brief(skill="art-director", subject="Ilustración editorial de portada")
result = generate_image(brief)
```

## Licencia

MIT. Ver [LICENSE](LICENSE).
