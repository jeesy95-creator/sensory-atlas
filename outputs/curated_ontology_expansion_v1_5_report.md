# Curated Ontology Expansion Batch 1 v1.5 Report

## Summary
- Previous main ontology object count: 50
- New promoted object count: 8
- New total object count: 58
- Deferred shortlist candidates: 4
- Phrase cue additions: 80 positive cues / 40 negative cues
- Regression case count: 32
- Evaluation results: default 1.00/1.00, blind 1.00/1.00, holdout 0.78/0.88

## Promoted Objects

| object_id | family | reason | related objects | risk |
| --- | --- | --- | --- | --- |
| green_leaf_crush | Organic | Fresh crushed-leaf archetype distinct from dry herb and wet moss. | green_stem, wet_moss, after_rain_garden | low |
| wet_soil | Organic | Low damp earth archetype distinct from wet stone and forest floor. | forest_floor, wet_moss, after_rain_garden, wet_stone | low |
| astringent_dryness | Texture | Reusable dry/gripping texture archetype for finish language. | black_tea, dry_herb, charred_oak | medium |
| amber_glow | Resin | Warm resinous golden glow with cross-domain sensory value. | honeycomb, vanilla_cream, pine_resin | low |
| dark_resin | Resin | Low dark resin archetype distinct from pine resin and tobacco leaf. | tobacco_leaf, forest_floor, charred_oak, pine_resin | medium |
| lactonic_milk_softness | Creamy | Milky rounded softness between cream, cotton, and skin-like comfort. | vanilla_cream, warm_cotton, cashmere | medium |
| tea_like_clarity | Tea | Dry clear tea-like transparency useful beyond beverage notes. | black_tea, dry_herb, fresh_linen | medium |
| golden_density | Gourmand | Density-first golden sweetness distinct from honeycomb and burnt sugar. | honeycomb, burnt_sugar, vanilla_cream | low |

## Deferred Candidates

| candidate_object_id | reason | next action |
| --- | --- | --- |
| fig_leaf_green | Potentially too fig/fruit-note-like; needs distinction from green_stem and honeycomb. | Review in a future curated batch before any merge. |
| stone_fruit_glow | Reads as a fruit note family; future batch candidate after more metaphorical cases. | Review in a future curated batch before any merge. |
| iodine_coast | Needs broader cross-domain evidence beyond coastal/medicinal language. | Review in a future curated batch before any merge. |
| syrupy_body | May belong as density/texture descriptor rather than standalone sensory object. | Review in a future curated batch before any merge. |

## Evaluation

| dataset | Top-1 | Top-3 | low-confidence |
| --- | --- | --- | --- |
| default | 1.00 | 1.00 | 0 |
| blind | 1.00 | 1.00 | 0 |
| holdout | 0.78 | 0.88 | 5 |

## Notes
- No holdout modification.
- No parser scoring modification.
- No matcher or cue hierarchy modification.
- No candidate auto-merge beyond the curated list.
- Deferred shortlist candidates remain reviewable for future batches.
