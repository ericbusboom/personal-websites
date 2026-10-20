+++
title = "Frame Model"
weight = 5
description = "Interactive 3D model of the steel frame, every member drawn at its actual cross-section"
+++

Every member is extruded at its actual cross-section, so relative sizes are
readable. Drag to rotate, scroll to zoom. Hover any member for its section,
utilisation and what governs it.

<div class="frame-embed">
  <iframe src="/structural/frame-model.html" title="Garage frame — interactive model" loading="lazy"></iframe>
</div>

<p style="text-align:center"><a href="/structural/frame-model.html"><strong>Open the model full screen →</strong></a></p>

<style>
  .frame-embed { position: relative; width: 100%; height: 78vh; min-height: 520px;
                 background: #fff; border: 1px solid var(--border);
                 border-radius: var(--radius); overflow: hidden; margin: 20px 0; }
  .frame-embed iframe { width: 100%; height: 100%; border: 0; display: block; }
</style>

## What the controls do

**Colour** switches between *how hard each member is working* — demand over
capacity under the governing combination — and *what governs it*, which family
of load combination produces the worst case.

**Checkboxes** toggle the existing garage walls and roof, the new frame, the
pre-demolition erection stage, and the loft layout with everything stored on it.
The existing roof starts hidden, because it sits between the new floor and the
new roof and hides most of what the model is for.

## Also here

- **[Frame plan](/structural/frame-plan.png)** — every member named and
  dimensioned, openings hatched
- **[STR-008 cost reduction study](/structural/STR-008-cost-reduction-study.md)**
  — the analysis behind the model
- **[06 · Structural Engineering](/06-structural/)** — the written section

> **Preliminary engineering study. Not a construction document.** No connection,
> base plate, anchor or foundation is designed or checked.
