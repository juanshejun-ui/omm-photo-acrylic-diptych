---
name: omm-photo-acrylic-diptych
description: Turn one or more supplied photographs into quiet 3:4 vertical art posters with the original photo preserved in the upper 50% and a tiny, source-derived hand-drawn acrylic abstraction on textured paper in the lower 50%. Use for photo-and-illustration diptychs, poetic wedding or travel covers, artist-book posters, and small-subject/large-negative-space editorial artwork; do not use for ordinary full-frame style transfer.
---

# OMM Photo Acrylic Diptych

Create one finished poster per input photo. Preserve the photograph as evidence; reinterpret it only in the lower panel.

## Non-negotiable visual system

- Final canvas: vertical 3:4.
- Division: one clean horizontal split at exactly 50% height.
- Upper panel: the user's original photograph, unchanged in content and photographic character. Preserve people, faces, architecture, animals, landscape, objects, light, color atmosphere, spatial relationships, and core composition.
- Lower panel: rough white, warm-white, cream, or pale art paper with visible fibers and tooth.
- Illustrated subject: a small, concentrated cluster occupying about 10–20% of the lower panel. Let empty paper dominate.
- Drawing: thin, slightly unstable hand-drawn lines that indicate structure without tracing every contour.
- Paint: at most four main colors sampled from the source photo. Use restrained, opaque acrylic shapes with dry-brush gaps, pigment drag, and lightly irregular edges.
- Relationship: lines suggest structure; color blocks establish the subject and hierarchy.
- Mood: quiet, playful, poetic, relaxed, tactile, sophisticated, and suitable for an artist's book or independent publication.

Avoid photorealistic repainting below, automatic line-art conversion, dense scenery, decorative templates, gradients, glossy digital vector shapes, oversized subjects, repeated motifs, borders, watermarks, and invented people or objects.

Text is optional. Default to no added text. If the user requests text, keep it very small and sparse below the illustration and reproduce the supplied wording verbatim.

## Workflow

1. Treat each user photo as an independent edit target and produce a separate poster. Never combine multiple source photos into one poster unless requested.
2. Inspect every local input image before generation. Identify the most recognizable subject, silhouette, pose/action, spatial relation, narrative relation, and one or two environmental cues.
3. Choose a maximum four-color palette from the source. Favor one high-contrast structural dark, the paper/ivory, and one or two meaningful accents.
4. Generate only the lower 3:2 illustration panel with the image generation tool. Use the source photo as a content reference and, when helpful, one or two bundled examples as style/spacing references. Label their roles explicitly. Read [references/style-spec.md](references/style-spec.md) for the prompt recipe and variation guidance.
5. Keep the generated lower-panel subject at 10–20% of that panel, with large uninterrupted negative space. Regenerate if the subject is too large, the palette exceeds four dominant colors, or the result resembles a traced miniature.
6. Compose the untouched source photo above the generated lower panel with `scripts/compose_diptych.py`. This deterministic composition step is required when pixel-faithful photo preservation matters; do not ask the image model to redraw the upper photo.
7. Verify the final canvas by integer dimensions: `width * 4 == height * 3`, and verify the split occurs at exactly half the pixel height. Visually inspect that the upper photo is unaltered apart from proportional scaling and optional paper-colored letterboxing.
8. Save final multi-image deliverables together with stable, source-derived filenames and report their paths.

## Composition rules

The upper panel is 3:2 landscape within the 3:4 poster. For landscape sources, scale proportionally to fit or minimally crop only when the user permits it. For portrait sources, fit the entire image and use paper-colored side margins; do not stretch or rotate it.

Place the lower illustration near the optical center or slightly below it. Preserve asymmetry from the source when it carries the story. Use at most a few environmental marks: one horizon, doorway, sun, tree, flower cluster, architectural arc, or similar cue. Do not fill the paper merely to balance the frame.

Bundled lower-panel examples in `assets/` demonstrate the intended family without including the original photographs. Use them for scale, restraint, texture, and negative space only; never copy their wedding subjects into unrelated photos.

## Deliverable standard

For each source, deliver one PNG poster. Prefer a width divisible by 3, such as 1800 × 2400. Keep generated drafts separate from final composites. If a generation misses the format or visual invariants, correct that asset before calling the set complete.
