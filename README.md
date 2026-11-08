# Tiento

![Tiento — art direction for AI images](docs/assets/hero-banner.png)

Tiento supports thoughtful, well-directed AI image generation across creative work. It helps structure the visual brief before you generate, so the image starts with clear intent.

## What it does

Tiento is a Hermes skill for shaping image concepts, composition, and visual style. Its guidance covers a range of creative work:

| Sub-skill | Use it to |
|---|---|
| `art-director/` | Develop a visual concept and art direction. |
| `interface-director/` | Plan the layout and visual style of an interface mockup. |
| `visual-critic/` | Review an existing mockup and prioritize improvements. |

## Getting started

Install the skill in Hermes:

```bash
hermes skills install https://raw.githubusercontent.com/lucio-homelab/tiento/main/SKILL.md
```

Then call `/tiento` with the kind of direction you need:

```text
/tiento Art-direct a 16:9 editorial illustration for a product announcement.
/tiento Plan a clear, welcoming interface mockup for a budgeting app.
/tiento Critique the attached dashboard mockup and prioritize the changes.
```

Tiento structures the visual brief and returns direction for your image-generation workflow. It does not include its own image renderer; rendering depends on the tools available in your Hermes session.

## Origin

Tiento adapts the `tiento` plugin from [`LucioB16/chatgpt-plugins`](https://github.com/LucioB16/chatgpt-plugins) (folder `tiento/`) into a Hermes skill.

## License

MIT. See [LICENSE](LICENSE).
