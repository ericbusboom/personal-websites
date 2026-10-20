+++
title = "06 · Structural Engineering"
weight = 60
description = "Beam-scheme steel frame: finite element analysis, member optimisation, and the interactive model"
+++

> **Preliminary engineering study. Not a construction document.** No connection,
> base plate, anchor or foundation is designed or checked. Nothing here may be
> built from until a California-licensed structural engineer has reviewed,
> signed and sealed the design.

## Interactive model

**[Open the frame model →](/structural/frame-model.html)**

Every member extruded at its actual cross-section, so relative sizes are
readable. Colour switches between how hard each member is working and what
governs it. Checkboxes toggle the existing garage walls and roof, the new
frame, the pre-demolition stage, and the loft layout.

**[Frame plan →](/structural/frame-plan.png)** — every member named and
dimensioned, openings hatched.

**[STR-008 cost reduction study (markdown) →](/structural/STR-008-cost-reduction-study.md)**

## STR-008: Frame cost reduction study

**Revision 3 · 2026-09-19 · Status: Draft**

**Scheme:** BEAM-001, `frame-20260920.01-beam-scheme`
**Live load:** 100 psf (DEC-014) · **Wind:** 96 mph, Exposure C
**Code:** 2022 CBC / ASCE 7-16 · **Software:** PyNite 3.2.0, COMPAS 2.15.1

The stored COMPAS model is the design. The owner revisions — the solar
slope seated on `B-SO`, `BE.upper`, the east side rebuilt in wood, the
stairwell moved south, `BWI-2`/`BWI-3` merged, the `N-M2` post and the
redundant bracing — are baked into it and listed in its `revisions` key,
with `baked_from` naming the model they started from. Opening the file
gives the frame as drawn here, not its starting point.

### The finding that reorders everything else

**Optimising this frame for weight optimises the cheapest thing in it.**

| Cost driver | Rate |
|---|---|
| Steel material | $0.77–0.94/lb — 1,000 lb is worth about $850 |
| Shop fitting and welding | $16–39 per joint |
| Field-bolted connections | $40–80 each |
| Erection, per piece | $55–95 |
| Procurement | $150–400 per **distinct section** |
| Shop fabrication minimum | $10,000–18,000 as a job charge |

The quantities that move money are **pieces, joints and distinct sections** —
not pounds. Removing a member deletes its joints, its handling and its
erection; thinning a member's wall deletes none of those.

### Verified package

| | As drawn | Recommended | Change |
|---|---|---|---|
| Steel | 9,718 lb | 8,047 lb | −1,671 lb |
| Pieces | 73 | **58** | −15 |
| Fitted joints | 135 | **104** | −31 |
| Distinct sections | 11 | **6** | −5 |
| Cost | $23,028–41,596 | $18,416–32,840 | **−$6,684** |
| Worst utilisation | 0.98 | **0.777** | — |
| Wind drift | H/464 | **H/434** | — |
| Deflection violations | 0 | 0 | — |

Every option was re-solved against each governing load combination and checked
for strength, span deflection **and** wind drift before being counted.

### Section palette

Collapsing to one section per structural role is the cheapest change available
— it adds steel and saves money, and the frame gets safer doing it.

| Role | Section |
|---|---|
| Columns | HSS5×5×1/4 |
| Truss | HSS3×3×1/8 |
| Clerestory and bracing | HSS2-1/2×2-1/2×1/8 |
| Rafters | HSS2×2×1/8 |

### No floor joist can be deleted

The joists carry the deck, and the deck is not in the structural model. Tested
one at a time against the 23/32 in. OSB span of 24 in., measured across each
deck **including out to its framed edges**: at 15.4 in. centres, removing one
joist doubles the span to about 31 in. There is no deletion that lands inside
24 in.

An earlier revision of this study proposed deleting 33 of 54 joists. That was a
defect in the deck-span check, not a finding — it would have left one shelf with
no framing at all and a 128 in. gap in a loft bay. The frame solver never
objected, because there are no plates in the model: with the joists gone the
tributary machinery handed the floor load straight to the beams, and the beams
could carry it.

**That is the standing limitation of this whole study.** A bare frame analysis
cannot tell whether there is anything left for the sheathing to sit on.

### Owner revisions carried

- **Stairwell moved one bay south** — `B-1A` runs west to `BW`, `B-1` is cut
  back. The opening moves from y 71–185 to y 3–128. Structurally free: steel,
  pieces and joints identical, because `B-1A` gains exactly the length `B-1`
  gives up.
- **`BWI-2` and `BWI-3` merged** into one continuous 182 in. `W12X16`. The
  splice had been left sitting in the middle of the free edge of the stair
  opening.
- **The vacated bay is framed, not just decked** — two 2×8 joists on the same
  stations as the bay north of it.
- **East side rebuilt in wood** and analysed as a separate structure. The steel
  frame transfers no load to the existing east wall; the lean-to hands 815 lb to
  `BE.upper` and the same to the wall.
- **Second north-wall post `N-M2`** at x = 16.75, cutting the loading opening to
  6 ft. Costs 45 lb and improves both utilisation and drift.

### Construction sequencing

**51 members can be erected before the existing roof comes off**, with 61
waiting. Four members penetrate the existing eave and need a hole rather than an
opening: `BWI-1`, `BWI-2`, `BWI-3` and `S3`.

### What still needs engineering

- Connection design for all 104 fitted joints
- Base plates, anchorage and foundation design
- Verification of the existing walls and slab for transferred loads
- The ASCE 7-16 §4.4 concentrated load check (ASM-011, open)
- Three San Diego shops quoted before any of these reductions are treated as
  money — the fabrication minimum may absorb part of them

### Limits

Gravity, wind and a seismic screening check only. Costs are parametric estimates
on this project's own rates, not quotations; the differences between options are
more reliable than the totals. Every reduction is conditional on the 100 psf
live load of DEC-014 and the concentrated equipment loads of ASM-011, which
remain open.
