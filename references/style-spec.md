# OMM lower-panel style specification

Read this reference when preparing the image-generation prompt for a lower illustration panel.

## Prompt recipe

Use case: `style-transfer`

Asset type: standalone lower illustration panel for an OMM 3:4 photo-and-acrylic diptych.

Input roles:

- User photo: content source. Extract only its key subject, gesture, relationship, environment cue, and palette.
- Bundled lower-panel example(s): style and spacing reference only. Do not copy their people, clothing, setting, or objects.

State all of these constraints in the prompt:

- Output a landscape 3:2 lower panel only; do not include the original photo or create a full poster.
- Background is warm white or pale fibrous art paper with visible grain.
- The subject cluster occupies only 10–20% of the panel.
- Use thin, slightly wavering hand-drawn lines and a few opaque matte acrylic shapes.
- Use no more than four dominant colors sampled from the source.
- Preserve recognizable pose, action, silhouette, and spatial/narrative relationship, but simplify aggressively.
- Add no more than one or two sparse environmental cues.
- Leave the large majority of the panel empty.
- No text unless exact copy is supplied; no watermark.
- Avoid realistic miniature painting, photo tracing, automatic line-art, gradients, glossy vector finish, complex background, frames, and template ornaments.

## Choosing what to retain

Retain the smallest set of evidence that makes the source recognizable:

- People: pose, direction of gaze, joined hands, relative scale, distinctive garment mass, or one carried object.
- Architecture: one silhouette, doorway, repeated vertical, arch, or roof line.
- Landscape: one horizon, peak rhythm, water line, tree silhouette, or path.
- Animals: species-defining silhouette, posture, direction, and relation to a person or setting.
- Detail photographs: one dominant plane, edge, scattered motif, or material contrast.

When the source is visually dense, compress groups into one shared gesture rather than drawing every face or object.

## Palette behavior

Count paper white as a support, not necessarily a paint color. A useful four-color structure is:

1. deep structural dark;
2. light subject color or ivory;
3. main emotional accent;
4. optional environmental accent.

Use the high-chroma accent sparingly but decisively. Let dry-brush breaks expose the paper.

## Variation without losing the family

Vary the tiny cluster's position, abstraction strategy, and environmental cue according to the photo. Keep the 50/50 architecture, paper family, scale restraint, line behavior, and matte acrylic texture consistent across a series.
