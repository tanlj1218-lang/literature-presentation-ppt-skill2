# Image2-to-Editable-PPT Workflow

## 1. Principle

Every slide is first designed as a page-specific image2/image_gen reference after its scientific content and logic are fixed. The generated image is then reconstructed element by element into an editable PPTX. The image is a visual blueprint, not the final slide.

## 2. Required order

1. Complete the full-deck blueprint.
2. Obtain content-architecture and style approval.
3. Complete the slide specification.
4. Generate a full-slide image2 reference for that exact page.
5. Generate separate transparent assets when needed.
6. Reconstruct the page with native PowerPoint objects.
7. Render and compare the PPT slide against the reference.
8. Complete the production manifest and QA.

## 3. Page-specific image generation

The prompt must include:

- page purpose;
- conclusion-style title intent;
- scientific logic;
- hierarchy of evidence and interpretation;
- exact layout family;
- source-figure aspect ratio or placeholder;
- reference/footer area;
- academic style constraints;
- prohibited visual elements.

Do not reuse one generic prompt for every page. Repeated visual DNA is desirable; repeated generic layouts are not.

## 4. Results pages

Use one source figure, one coherent figure panel, one native table, or one analytical conclusion per slide. The image2 reference should visually reserve:

- 55–70% for the evidence when the figure is central;
- an adjacent interpretation block;
- a small source note;
- no unrelated secondary figure.

Never ask image generation to redraw exact statistical charts. Use the verified original figure or a native chart in the final PPT.

## 5. Element-level reconstruction

Rebuild:

- background and navigation with native shapes;
- every formal sentence with native text boxes;
- arrows and connectors with native lines;
- tables and charts with native editable objects;
- complex source figures with verified high-resolution crops;
- complex illustrative assets with transparent generated images.

The full-slide generated image must never be inserted as a single background picture.

## 6. Coordinate mapping

For a 16:9 reference image, map image coordinates to slide coordinates:

- x_ppt = x_image / image_width × slide_width;
- y_ppt = y_image / image_height × slide_height;
- w_ppt = w_image / image_width × slide_width;
- h_ppt = h_image / image_height × slide_height.

Correct obvious image-generation distortions rather than copying them blindly.

## 7. Fidelity check

Compare the generated reference and rendered PPT side by side. Check:

- hierarchy;
- relative position and scale;
- spacing and negative space;
- reading path;
- color and visual rhythm;
- figure prominence;
- reference placement;
- text correctness;
- editability.

A visually similar but scientifically inaccurate reconstruction fails. A scientifically correct but visually unrelated reconstruction also fails.
