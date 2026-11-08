# Tiento

![Tiento — art direction for AI images](docs/assets/hero-banner.png)

Tiento supports thoughtful, well-directed AI image generation across creative work by structuring the brief before you generate. Capture the subject, audience, medium, aspect ratio, exclusions, and references that guide your visual direction.

## What it does

Tiento is a Hermes skill for shaping the visual direction behind AI-generated images. It organizes the work into three focused sub-skills:

| Sub-skill | Role |
|---|---|
| `art-director/` | Develops an art direction and visual concept. |
| `interface-director/` | Designs interfaces and mockups. |
| `visual-critic/` | Critiques visual mockups. |

## Getting started

Clone the repository and list the available sub-skills:

```bash
git clone https://github.com/lucio-homelab/tiento.git
cd tiento
python3 tiento.py --list
```

Validate the skill definitions and run the tests:

```bash
python3 tiento.py --validate
python3 tests/test_tiento.py
```

Tiento requires Python 3 and uses only the standard library; no package installation is required.

## Build a brief

Use `build_brief()` to create a structured direction for a visual:

```python
from tiento import build_brief

brief = build_brief(
    skill="art-director",
    subject="Cover illustration for a product announcement",
    audience="product team",
    medium="digital",
    aspect_ratio="16:9",
    exclusions=["generic gradients", "stock-photo look"],
    references=["brand-guidelines.pdf"],
)

print(brief.to_json(indent=2))
```

A brief records the target sub-skill, subject, optional audience and medium, aspect ratio, exclusions, and references.

## Python API

- `list_skills()` returns the available sub-skills and their descriptions.
- `build_brief(...)` creates a validated `Brief`; it raises `UnknownSkillError` for an unknown sub-skill.
- `Brief.to_dict()` and `Brief.to_json()` serialize a brief.
- `generate_image(brief)` is a placeholder and does not render an image yet.

## Project status

Tiento currently provides structured briefs, sub-skill selection, and validation. Use its briefs to guide your chosen image-generation workflow; rendering is not implemented yet.

## Origin

Tiento adapts the `tiento` plugin from [`LucioB16/chatgpt-plugins`](https://github.com/LucioB16/chatgpt-plugins) (folder `tiento/`) into a Hermes skill.

## License

MIT. See [LICENSE](LICENSE).
