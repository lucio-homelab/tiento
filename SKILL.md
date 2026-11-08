---
name: tiento
version: 0.1.0
description: Art direction for thoughtful AI image generation.
author: LucioB16
license: MIT
---

# Tiento

Tiento helps shape the visual direction behind AI-generated images. It creates a clear, prompt-ready brief; it does not render images by itself.

## When to Use

- Develop a visual concept or art direction for an image.
- Plan the composition, visual style, and framing for an image-generation workflow.
- Design an interface mockup concept.
- Critique an existing image or mockup.

## Procedure

1. Identify whether the request is for art direction, an interface mockup, or a visual critique. Combine these only when the user asks for it.
2. Gather the details that materially affect the direction: subject, purpose, audience, medium, aspect ratio, references, and exclusions. Ask only for missing details that cannot be reasonably inferred.
3. For art direction, return a concept, composition and focal hierarchy, visual style, palette or lighting where relevant, framing, and exclusions.
4. For interface mockups, describe the user task, screen hierarchy, layout, key components, and visual style. Do not present a concept as a working interface.
5. For critiques, ground each finding in visible details and prioritize the changes by impact.
6. If the user asks to render an image and an image-generation tool is available, use it. Otherwise, return a prompt-ready direction and make clear that no image was rendered.

## Modes of Work

- Art direction develops a visual concept and composition.
- Interface direction plans layouts and mockups.
- Visual critique reviews existing images and mockups.

## Verification

Before returning a direction, check that it matches the brief, states a usable composition and style, respects the requested format and exclusions, and distinguishes a prompt or concept from a rendered image.

## Origin

Tiento adapts the `tiento` plugin from [`LucioB16/chatgpt-plugins`](https://github.com/LucioB16/chatgpt-plugins) (folder `tiento/`).
