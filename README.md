# Skill Tiento

Adaptación del plugin ChatGPT `tiento` del repositorio
[github.com/LucioB16/chatgpt-plugins](https://github.com/LucioB16/chatgpt-plugins),
llevado como skill de Hermes para generación de imágenes IA tasteful para
LinkedIn.

## Contenido

- `SKILL.md` — definición del skill con frontmatter YAML (formato Hermes).
- `tiento.py` — CLI ejecutable con `--list` y `--validate`.
- `tests/test_tiento.py` — 4 tests de unidad.
- `art-director/`, `interface-director/`, `visual-critic/` — sub-skills.
- `LICENSE` — MIT.

## Uso

```bash
python tiento.py --list
python tiento.py --validate
python -m pytest tests/
```

## Origen

Este skill es una adaptación del plugin `tiento` publicado originalmente en
el repositorio `github.com/LucioB16/chatgpt-plugins` del usuario LucioB16.

## Licencia

MIT.