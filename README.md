# Tiento

Tiento supports thoughtful, well-directed AI image generation across creative work. It turns a brief into structured image direction — concept, composition, and visual style — so imagery feels intentional rather than generic.

![Tiento hero banner](docs/assets/hero-banner.png)

![Tiento mark (dark)](docs/assets/tiento-mark-dark.png "Tiento mark — dark variant")
![Tiento mark (light)](docs/assets/tiento-mark-light.png "Tiento mark — light variant")

## The problem

AI image generation can produce polished images that still feel generic when the direction is unclear. Without a point of view, compositions and visual language can drift.

Tiento helps shape the direction behind generated images. As a Hermes skill, it provides structured briefs, skill routing, and a generation skeleton to support intentional visual choices across subjects, formats, and creative workflows.

## What's inside

Tiento is organized as three sub-skills, each owning one stage of the visual direction:

| Sub-skill | Role |
|---|---|
| `art-director/` | Art direction and visual concept |
| `interface-director/` | Interface design and mockups |
| `visual-critic/` | Visual critique of mockups |

Each sub-skill is a directory with its own README describing inputs, outputs, and conventions.

## Conceptual preview

Tiento routes a creative brief through a sub-skill and produces a structured direction. The diagram below is a conceptual SVG (generable with `scripts/preview_concepts.py` when available) showing the flow.

```text
Brief ──► [ skill selection ] ──► [ art direction ] ──► Image direction
```

## Getting started

```bash
# Clone the repository
git clone https://github.com/lucio-homelab/tiento.git
cd tiento

# List the available sub-skills
python tiento.py --list

# Validate the skill definitions
python tiento.py --validate

# Run the unit tests (4 tests)
python tests/test_tiento.py
```

### Building a brief from Python

```python
from tiento import build_brief, list_skills

# See available sub-skills
print(list_skills())
# {'art-director': 'Art direction and visual concept.',
#  'interface-director': 'Interface design and mockups.',
#  'visual-critic': 'Visual critique of mockups.'}

# Build a brief for the art-director sub-skill
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

## Usage

### CLI

```bash
python tiento.py --list
python tiento.py --validate
```

### Python API

```python
from tiento import Brief, UnknownSkillError, build_brief, generate_image, list_skills

# List sub-skills
skills = list_skills()

# Build a validated brief
brief = build_brief(
    skill="visual-critic",
    subject="Dashboard mockup review",
    audience="design team",
    medium="screen",
    aspect_ratio="4:3",
)

# Generate (skeleton — see Project status below)
result = generate_image(brief)
print(result)
```

## Technical reference

### `list_skills() -> dict[str, str]`

Returns the available sub-skills mapped to their descriptions.

### `build_brief(skill, subject, audience=None, medium=None, aspect_ratio=None, exclusions=None, references=None) -> Brief`

Builds and validates a `Brief` for the given sub-skill. Raises `UnknownSkillError` if the skill does not exist.

### `generate_image(brief: Brief) -> str`

Skeleton generation entry point. Accepts a `Brief` and returns a placeholder message indicating the sub-skill is a skeleton pending implementation.

### `Brief` dataclass

| Field | Type | Description |
|---|---|---|
| `skill` | `str` | Target sub-skill name |
| `subject` | `str` | Brief subject / creative prompt |
| `audience` | `str \| None` | Intended audience |
| `medium` | `str \| None` | Delivery medium |
| `aspect_ratio` | `str \| None` | Target aspect ratio |
| `exclusions` | `list[str]` | Visual elements to exclude |
| `references` | `list[str]` | Reference assets |

`Brief.to_dict()` returns a plain dict; `Brief.to_json(**kwargs)` returns a JSON string.

### `UnknownSkillError(ValueError)`

Raised by `build_brief` when the requested sub-skill is not registered.

## Project status (honest)

Tiento is currently a **skeleton**:

- ✅ `list_skills()`, `build_brief()`, `generate_image()` exist and are typed
- ✅ `Brief` dataclass with `to_dict()` / `to_json()`
- ✅ `--list` and `--validate` CLI commands
- ✅ 4 unit tests, all passing
- ❌ `generate_image()` does not render images yet — it returns a placeholder message
- ❌ No real image-rendering backend is wired in

The roadmap is to move from skeleton to a real rendering path: connect an image-generation provider, add output validation, and let each sub-skill produce actual visuals. Until then, Tiento gives you the structure (briefs, routing, validation) so the rendering layer has a solid contract to build against.

## Origin

Tiento is an adaptation of the `tiento` plugin from [`github.com/LucioB16/chatgpt-plugins`](https://github.com/LucioB16/chatgpt-plugins) (folder `tiento/`), ported as a Hermes skill by LucioB16.

## License

MIT. See [LICENSE](LICENSE).
