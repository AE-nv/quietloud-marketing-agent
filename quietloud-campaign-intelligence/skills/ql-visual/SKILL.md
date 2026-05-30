---
name: ql-visual
description: Generate visual direction, layout notes, and an image prompt for the campaign asset.
---

# Graphical Pipeline

## Role

Seventh step in the QuietLoud pipeline. Produce visual direction for the campaign asset and generate an image if possible.

## Background

Use context from `quietloud-background` for QuietLoud's visual identity, brand style, and design principles.

## Input

- `generation_plan` — from `ql-execution`
- `persona` — from `ql-profile`
- `method` — from `ql-method`

## Task

Produce visual direction suited to the method and persona. Then generate a detailed image prompt for Codex image generation.

For LinkedIn: social-native, clean, attention-stopping.
For email: professional, uncluttered, mobile-readable.
For website blocks: conversion-focused, brand-consistent.

Optionally: call Codex built-in image generation with the `image_prompt`.

## Output

```json
{
  "style_direction": "string",
  "layout_notes": "string",
  "image_prompt": "string"
}
```

## Rules

- `image_prompt` must be specific and visual — describe what is actually in the image, not a concept
- `style_direction` should reference colour mood, typography feel, and overall aesthetic
