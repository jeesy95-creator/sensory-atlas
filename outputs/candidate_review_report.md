# Candidate Sensory Object Review Report

## Summary
- Total candidates: 47
- defer_to_future_batch: 4
- do_not_merge_yet: 0
- keep_as_axis_descriptor: 0
- keep_as_candidate: 18
- needs_distinction_review: 12
- needs_more_examples: 0
- ready_for_curated_merge: 13

## High-Priority Candidates

| candidate_object_id | korean_label | source_domains | recommended_action | readiness_score | note_dictionary_risk |
| --- | --- | --- | --- | --- | --- |
| amber_glow | 앰버의 따뜻한 금빛 잔향 | fragrance, cross_domain | ready_for_curated_merge | 0.72 | 0.13 |
| lactonic_milk_softness | 우유처럼 하얗고 둥근 부드러움 | fragrance, coffee, cross_domain | ready_for_curated_merge | 0.80 | 0.00 |
| tea_like_clarity | 차처럼 맑고 건조한 투명감 | coffee, fragrance, cross_domain | ready_for_curated_merge | 0.80 | 0.00 |
| astringent_dryness | 혀를 조이는 수렴성 드라이함 | coffee, wine, cross_domain | ready_for_curated_merge | 0.74 | 0.15 |
| wet_soil | 비 맞은 흙의 낮고 축축한 냄새 | fragrance, wine, coffee, cross_domain | ready_for_curated_merge | 0.75 | 0.15 |
| golden_density | 금빛으로 두껍게 남는 달콤한 밀도 | fragrance, whisky, coffee, cross_domain | ready_for_curated_merge | 0.81 | 0.00 |
| dark_resin | 어둡고 낮게 깔리는 수지감 | fragrance, cross_domain | ready_for_curated_merge | 0.74 | 0.00 |
| green_leaf_crush | 잎을 으깼을 때 나는 아삭한 초록감 | fragrance, wine, coffee, cross_domain | ready_for_curated_merge | 0.75 | 0.15 |

## Ready for Curated Merge

### amber_glow / 앰버의 따뜻한 금빛 잔향
- definition: A warm golden resinous glow with soft sweetness and lingering density.
- core axes: `{"temperature": "Warm", "texture": ["Soft", "Dry"], "light": ["Diffuse"], "atmosphere": ["Muted"]}`
- example expressions: 앰버처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 앰버의 따뜻한 금빛 잔향에 가까운 느낌, 입안과 공기 중에 앰버의 분위기가 천천히 남는다
- suggested phrase cues: 앰버, 앰버 따뜻한 금빛 잔향, 앰버 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: honeycomb, vanilla_cream
- similar existing objects: [{"existing_object_id": "vanilla_cream", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.4}, {"existing_object_id": "honeycomb", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.38}, {"existing_object_id": "amber_glow", "similarity_reason": ["family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.16}, {"existing_object_id": "dark_resin", "similarity_reason": ["family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.14}, {"existing_object_id": "cashmere", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}]

```json
{
  "object_id": "amber_glow",
  "label": "Amber Glow",
  "korean_label": "앰버의 따뜻한 금빛 잔향",
  "object_type": "sensory_object_draft",
  "family": "Amber / Resin / Golden",
  "definition": "A warm golden resinous glow with soft sweetness and lingering density.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Soft",
      "Dry"
    ],
    "light": [
      "Diffuse"
    ],
    "atmosphere": [
      "Muted"
    ]
  },
  "example_expressions": [
    "앰버처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 앰버의 따뜻한 금빛 잔향에 가까운 느낌",
    "입안과 공기 중에 앰버의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "honeycomb",
    "vanilla_cream"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

### powder_cloud / 가루처럼 부드럽게 흐려지는 구름감
- definition: A muted powdery softness that diffuses edges and leaves a dry cosmetic haze.
- core axes: `{"temperature": "Warm", "texture": ["Soft", "Dry"], "light": ["Diffuse"], "atmosphere": ["Muted"]}`
- example expressions: 가루처럼 부드럽게 흐려지는 구름감처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 가루처럼 부드럽게 흐려지는 구름감에 가까운 느낌, 입안과 공기 중에 가루처럼 부드럽게 흐려지는 구름감의 분위기가 천천히 남는다
- suggested phrase cues: 가루처럼 부드럽게 흐려지는 구름감, 가루처럼 부드럽게 흐려지는 구름감, 가루처럼 부드럽게 흐려지는 구름감 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: velvet, warm_cotton
- similar existing objects: [{"existing_object_id": "warm_cotton", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.41}, {"existing_object_id": "velvet", "similarity_reason": ["related_existing_object", "axis_overlap"], "overlap_score": 0.4}, {"existing_object_id": "cashmere", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "wool_blanket", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "film_grain", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}]

```json
{
  "object_id": "powder_cloud",
  "label": "Powder Cloud",
  "korean_label": "가루처럼 부드럽게 흐려지는 구름감",
  "object_type": "sensory_object_draft",
  "family": "Powdery / Soft / Muted",
  "definition": "A muted powdery softness that diffuses edges and leaves a dry cosmetic haze.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Soft",
      "Dry"
    ],
    "light": [
      "Diffuse"
    ],
    "atmosphere": [
      "Muted"
    ]
  },
  "example_expressions": [
    "가루처럼 부드럽게 흐려지는 구름감처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 가루처럼 부드럽게 흐려지는 구름감에 가까운 느낌",
    "입안과 공기 중에 가루처럼 부드럽게 흐려지는 구름감의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "velvet",
    "warm_cotton"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

### lactonic_milk_softness / 우유처럼 하얗고 둥근 부드러움
- definition: A white creamy softness with gentle warmth and low edges.
- core axes: `{"temperature": "Warm", "texture": ["Soft", "Dry"], "light": ["Diffuse"], "atmosphere": ["Muted"]}`
- example expressions: 우유처럼 하얗고 둥근 부드러움처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 우유처럼 하얗고 둥근 부드러움에 가까운 느낌, 입안과 공기 중에 우유처럼 하얗고 둥근 부드러움의 분위기가 천천히 남는다
- suggested phrase cues: 우유처럼 하얗고 둥근 부드러움, 우유처럼 하얗고 둥근 부드러움, 우유처럼 하얗고 둥근 부드러움 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: vanilla_cream, warm_cotton
- similar existing objects: [{"existing_object_id": "warm_cotton", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.41}, {"existing_object_id": "vanilla_cream", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.41}, {"existing_object_id": "lactonic_milk_softness", "similarity_reason": ["family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.15}, {"existing_object_id": "cashmere", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "wool_blanket", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}]

```json
{
  "object_id": "lactonic_milk_softness",
  "label": "Lactonic Milk Softness",
  "korean_label": "우유처럼 하얗고 둥근 부드러움",
  "object_type": "sensory_object_draft",
  "family": "Milky / Creamy / Soft",
  "definition": "A white creamy softness with gentle warmth and low edges.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Soft",
      "Dry"
    ],
    "light": [
      "Diffuse"
    ],
    "atmosphere": [
      "Muted"
    ]
  },
  "example_expressions": [
    "우유처럼 하얗고 둥근 부드러움처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 우유처럼 하얗고 둥근 부드러움에 가까운 느낌",
    "입안과 공기 중에 우유처럼 하얗고 둥근 부드러움의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "vanilla_cream",
    "warm_cotton"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

### sherry_dried_fruit / 셰리 캐스크의 어두운 말린 과일감
- definition: A dense dried-fruit sweetness with dark cask warmth and aged depth.
- core axes: `{"temperature": "Warm", "texture": ["Juicy", "Soft"], "light": ["Bright"], "atmosphere": ["Fresh"]}`
- example expressions: 셰리 캐스크처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 셰리 캐스크의 어두운 말린 과일감에 가까운 느낌, 입안과 공기 중에 셰리 캐스크의 분위기가 천천히 남는다
- suggested phrase cues: 셰리 캐스크, 셰리 캐스크 어두운 말린 과일감, 셰리 캐스크 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: dark_chocolate, tobacco_leaf, barrel_cellar
- similar existing objects: [{"existing_object_id": "dark_chocolate", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.38}, {"existing_object_id": "tobacco_leaf", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.38}, {"existing_object_id": "barrel_cellar", "similarity_reason": ["related_existing_object"], "overlap_score": 0.35}, {"existing_object_id": "warm_cotton", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.06}, {"existing_object_id": "film_grain", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.06}]

```json
{
  "object_id": "sherry_dried_fruit",
  "label": "Sherry Dried Fruit",
  "korean_label": "셰리 캐스크의 어두운 말린 과일감",
  "object_type": "sensory_object_draft",
  "family": "Dried Fruit / Aged / Dense",
  "definition": "A dense dried-fruit sweetness with dark cask warmth and aged depth.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Juicy",
      "Soft"
    ],
    "light": [
      "Bright"
    ],
    "atmosphere": [
      "Fresh"
    ]
  },
  "example_expressions": [
    "셰리 캐스크처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 셰리 캐스크의 어두운 말린 과일감에 가까운 느낌",
    "입안과 공기 중에 셰리 캐스크의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "dark_chocolate",
    "tobacco_leaf",
    "barrel_cellar"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

### wax_polish / 왁스로 닦은 오래된 표면의 윤기
- definition: A smooth waxed-surface glow that feels old, polished, and quiet.
- core axes: `{"temperature": "Warm", "texture": ["Soft", "Dry"], "light": ["Diffuse"], "atmosphere": ["Muted"]}`
- example expressions: 왁스로 닦은 오래된 표면처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 왁스로 닦은 오래된 표면의 윤기에 가까운 느낌, 입안과 공기 중에 왁스로 닦은 오래된 표면의 분위기가 천천히 남는다
- suggested phrase cues: 왁스로 닦은 오래된 표면, 왁스로 닦은 오래된 표면 윤기, 왁스로 닦은 오래된 표면 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: old_library, silver_spoon
- similar existing objects: [{"existing_object_id": "old_library", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.38}, {"existing_object_id": "silver_spoon", "similarity_reason": ["related_existing_object"], "overlap_score": 0.35}, {"existing_object_id": "cashmere", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "wool_blanket", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "film_grain", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}]

```json
{
  "object_id": "wax_polish",
  "label": "Wax Polish",
  "korean_label": "왁스로 닦은 오래된 표면의 윤기",
  "object_type": "sensory_object_draft",
  "family": "Wax / Polish / Smooth",
  "definition": "A smooth waxed-surface glow that feels old, polished, and quiet.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Soft",
      "Dry"
    ],
    "light": [
      "Diffuse"
    ],
    "atmosphere": [
      "Muted"
    ]
  },
  "example_expressions": [
    "왁스로 닦은 오래된 표면처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 왁스로 닦은 오래된 표면의 윤기에 가까운 느낌",
    "입안과 공기 중에 왁스로 닦은 오래된 표면의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "old_library",
    "silver_spoon"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

### black_fruit_density / 검은 과일의 두꺼운 밀도
- definition: A dark fruit density that feels ripe, thick, and low.
- core axes: `{"temperature": "Warm", "texture": ["Juicy", "Soft"], "light": ["Bright"], "atmosphere": ["Fresh"]}`
- example expressions: 검은 과일처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 검은 과일의 두꺼운 밀도에 가까운 느낌, 입안과 공기 중에 검은 과일의 분위기가 천천히 남는다
- suggested phrase cues: 검은 과일, 검은 과일 두꺼운 밀도, 검은 과일 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: dark_chocolate, honeycomb
- similar existing objects: [{"existing_object_id": "dark_chocolate", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.39}, {"existing_object_id": "honeycomb", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.38}, {"existing_object_id": "warm_cotton", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.06}, {"existing_object_id": "wool_blanket", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.06}, {"existing_object_id": "film_grain", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.06}]

```json
{
  "object_id": "black_fruit_density",
  "label": "Black Fruit Density",
  "korean_label": "검은 과일의 두꺼운 밀도",
  "object_type": "sensory_object_draft",
  "family": "Fruit / Dense / Dark",
  "definition": "A dark fruit density that feels ripe, thick, and low.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Juicy",
      "Soft"
    ],
    "light": [
      "Bright"
    ],
    "atmosphere": [
      "Fresh"
    ]
  },
  "example_expressions": [
    "검은 과일처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 검은 과일의 두꺼운 밀도에 가까운 느낌",
    "입안과 공기 중에 검은 과일의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "dark_chocolate",
    "honeycomb"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

### tea_like_clarity / 차처럼 맑고 건조한 투명감
- definition: A tea-like clear dryness with gentle bitterness and clean edges.
- core axes: `{"temperature": "Warm", "texture": ["Soft", "Dry"], "light": ["Diffuse"], "atmosphere": ["Muted"]}`
- example expressions: 차처럼 맑고 건조한 투명감처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 차처럼 맑고 건조한 투명감에 가까운 느낌, 입안과 공기 중에 차처럼 맑고 건조한 투명감의 분위기가 천천히 남는다
- suggested phrase cues: 차처럼 맑고 건조한 투명감, 차처럼 맑고 건조한 투명감, 차처럼 맑고 건조한 투명감 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: black_tea, dry_herb
- similar existing objects: [{"existing_object_id": "black_tea", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.41}, {"existing_object_id": "dry_herb", "similarity_reason": ["related_existing_object"], "overlap_score": 0.38}, {"existing_object_id": "tea_like_clarity", "similarity_reason": ["family_overlap", "keyword_overlap"], "overlap_score": 0.12}, {"existing_object_id": "cashmere", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "wool_blanket", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}]

```json
{
  "object_id": "tea_like_clarity",
  "label": "Tea-like Clarity",
  "korean_label": "차처럼 맑고 건조한 투명감",
  "object_type": "sensory_object_draft",
  "family": "Tea / Clarity / Dry",
  "definition": "A tea-like clear dryness with gentle bitterness and clean edges.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Soft",
      "Dry"
    ],
    "light": [
      "Diffuse"
    ],
    "atmosphere": [
      "Muted"
    ]
  },
  "example_expressions": [
    "차처럼 맑고 건조한 투명감처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 차처럼 맑고 건조한 투명감에 가까운 느낌",
    "입안과 공기 중에 차처럼 맑고 건조한 투명감의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "black_tea",
    "dry_herb"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

### astringent_dryness / 혀를 조이는 수렴성 드라이함
- definition: A drying astringent grip similar to tea leaves, tannin, or skins.
- core axes: `{"temperature": "Warm", "texture": ["Soft", "Dry"], "light": ["Diffuse"], "atmosphere": ["Muted"]}`
- example expressions: 혀를 조이는 수렴성 드라이함처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 혀를 조이는 수렴성 드라이함에 가까운 느낌, 입안과 공기 중에 혀를 조이는 수렴성 드라이함의 분위기가 천천히 남는다
- suggested phrase cues: 혀를 조이는 수렴성 드라이함, 혀를 조이는 수렴성 드라이함, 혀를 조이는 수렴성 드라이함 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: black_tea, charred_oak
- similar existing objects: [{"existing_object_id": "black_tea", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.41}, {"existing_object_id": "charred_oak", "similarity_reason": ["related_existing_object", "axis_overlap"], "overlap_score": 0.4}, {"existing_object_id": "cashmere", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "wool_blanket", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "film_grain", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}]

```json
{
  "object_id": "astringent_dryness",
  "label": "Astringent Dryness",
  "korean_label": "혀를 조이는 수렴성 드라이함",
  "object_type": "sensory_object_draft",
  "family": "Astringent / Dry / Grip",
  "definition": "A drying astringent grip similar to tea leaves, tannin, or skins.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Soft",
      "Dry"
    ],
    "light": [
      "Diffuse"
    ],
    "atmosphere": [
      "Muted"
    ]
  },
  "example_expressions": [
    "혀를 조이는 수렴성 드라이함처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 혀를 조이는 수렴성 드라이함에 가까운 느낌",
    "입안과 공기 중에 혀를 조이는 수렴성 드라이함의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "black_tea",
    "charred_oak"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

### wet_soil / 비 맞은 흙의 낮고 축축한 냄새
- definition: A low damp soil impression after rain, earthier than wet stone and less leafy than moss.
- core axes: `{"temperature": "Warm", "texture": ["Soft", "Dry"], "light": ["Diffuse"], "atmosphere": ["Muted"]}`
- example expressions: 비 맞은 흙처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 비 맞은 흙의 낮고 축축한 냄새에 가까운 느낌, 입안과 공기 중에 비 맞은 흙의 분위기가 천천히 남는다
- suggested phrase cues: 비 맞은 흙, 비 맞은 흙 낮고 축축한 냄새, 비 맞은 흙 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: forest_floor, after_rain_garden
- similar existing objects: [{"existing_object_id": "after_rain_garden", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.39}, {"existing_object_id": "forest_floor", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.36}, {"existing_object_id": "cashmere", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "wool_blanket", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "film_grain", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}]

```json
{
  "object_id": "wet_soil",
  "label": "Wet Soil",
  "korean_label": "비 맞은 흙의 낮고 축축한 냄새",
  "object_type": "sensory_object_draft",
  "family": "Earth / Rain / Moist",
  "definition": "A low damp soil impression after rain, earthier than wet stone and less leafy than moss.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Soft",
      "Dry"
    ],
    "light": [
      "Diffuse"
    ],
    "atmosphere": [
      "Muted"
    ]
  },
  "example_expressions": [
    "비 맞은 흙처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 비 맞은 흙의 낮고 축축한 냄새에 가까운 느낌",
    "입안과 공기 중에 비 맞은 흙의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "forest_floor",
    "after_rain_garden"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

### cosmetic_powder / 화장품 파우더의 매트한 잔향
- definition: A matte cosmetic powder with floral softness and dry surface feel.
- core axes: `{"temperature": "Warm", "texture": ["Soft", "Dry"], "light": ["Diffuse"], "atmosphere": ["Muted"]}`
- example expressions: 화장품 파우더처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 화장품 파우더의 매트한 잔향에 가까운 느낌, 입안과 공기 중에 화장품 파우더의 분위기가 천천히 남는다
- suggested phrase cues: 화장품 파우더, 화장품 파우더 매트한 잔향, 화장품 파우더 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: velvet, dry_herb
- similar existing objects: [{"existing_object_id": "velvet", "similarity_reason": ["related_existing_object", "axis_overlap"], "overlap_score": 0.4}, {"existing_object_id": "dry_herb", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.38}, {"existing_object_id": "cashmere", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "wool_blanket", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "film_grain", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}]

```json
{
  "object_id": "cosmetic_powder",
  "label": "Cosmetic Powder",
  "korean_label": "화장품 파우더의 매트한 잔향",
  "object_type": "sensory_object_draft",
  "family": "Cosmetic / Powdery / Matte",
  "definition": "A matte cosmetic powder with floral softness and dry surface feel.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Soft",
      "Dry"
    ],
    "light": [
      "Diffuse"
    ],
    "atmosphere": [
      "Muted"
    ]
  },
  "example_expressions": [
    "화장품 파우더처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 화장품 파우더의 매트한 잔향에 가까운 느낌",
    "입안과 공기 중에 화장품 파우더의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "velvet",
    "dry_herb"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

### golden_density / 금빛으로 두껍게 남는 달콤한 밀도
- definition: A golden dense sweetness that feels thicker than simple sugar.
- core axes: `{"temperature": "Warm", "texture": ["Soft", "Dry"], "light": ["Diffuse"], "atmosphere": ["Muted"]}`
- example expressions: 금빛으로 두껍게 남는 달콤한 밀도처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 금빛으로 두껍게 남는 달콤한 밀도에 가까운 느낌, 입안과 공기 중에 금빛으로 두껍게 남는 달콤한 밀도의 분위기가 천천히 남는다
- suggested phrase cues: 금빛으로 두껍게 남는 달콤한 밀도, 금빛으로 두껍게 남는 달콤한 밀도, 금빛으로 두껍게 남는 달콤한 밀도 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: honeycomb, burnt_sugar, vanilla_cream
- similar existing objects: [{"existing_object_id": "vanilla_cream", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.4}, {"existing_object_id": "honeycomb", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.39}, {"existing_object_id": "burnt_sugar", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.38}, {"existing_object_id": "cashmere", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "wool_blanket", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}]

```json
{
  "object_id": "golden_density",
  "label": "Golden Density",
  "korean_label": "금빛으로 두껍게 남는 달콤한 밀도",
  "object_type": "sensory_object_draft",
  "family": "Golden / Sweet / Dense",
  "definition": "A golden dense sweetness that feels thicker than simple sugar.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Soft",
      "Dry"
    ],
    "light": [
      "Diffuse"
    ],
    "atmosphere": [
      "Muted"
    ]
  },
  "example_expressions": [
    "금빛으로 두껍게 남는 달콤한 밀도처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 금빛으로 두껍게 남는 달콤한 밀도에 가까운 느낌",
    "입안과 공기 중에 금빛으로 두껍게 남는 달콤한 밀도의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "honeycomb",
    "burnt_sugar",
    "vanilla_cream"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

### dark_resin / 어둡고 낮게 깔리는 수지감
- definition: A dark resinous depth with earthy sweetness and low atmosphere.
- core axes: `{"temperature": "Warm", "texture": ["Soft", "Dry"], "light": ["Diffuse"], "atmosphere": ["Muted"]}`
- example expressions: 어둡고 낮게 깔리는 수지감처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 어둡고 낮게 깔리는 수지감에 가까운 느낌, 입안과 공기 중에 어둡고 낮게 깔리는 수지감의 분위기가 천천히 남는다
- suggested phrase cues: 어둡고 낮게 깔리는 수지감, 어둡고 낮게 깔리는 수지감, 어둡고 낮게 깔리는 수지감 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: tobacco_leaf, forest_floor, charred_oak
- similar existing objects: [{"existing_object_id": "tobacco_leaf", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.41}, {"existing_object_id": "charred_oak", "similarity_reason": ["related_existing_object", "axis_overlap"], "overlap_score": 0.4}, {"existing_object_id": "forest_floor", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.36}, {"existing_object_id": "dark_resin", "similarity_reason": ["family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.15}, {"existing_object_id": "amber_glow", "similarity_reason": ["family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.14}]

```json
{
  "object_id": "dark_resin",
  "label": "Dark Resin",
  "korean_label": "어둡고 낮게 깔리는 수지감",
  "object_type": "sensory_object_draft",
  "family": "Dark / Resin / Earth",
  "definition": "A dark resinous depth with earthy sweetness and low atmosphere.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Soft",
      "Dry"
    ],
    "light": [
      "Diffuse"
    ],
    "atmosphere": [
      "Muted"
    ]
  },
  "example_expressions": [
    "어둡고 낮게 깔리는 수지감처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 어둡고 낮게 깔리는 수지감에 가까운 느낌",
    "입안과 공기 중에 어둡고 낮게 깔리는 수지감의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "tobacco_leaf",
    "forest_floor",
    "charred_oak"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

### green_leaf_crush / 잎을 으깼을 때 나는 아삭한 초록감
- definition: A crushed green leaf sensation with cool moisture and crisp vegetal snap.
- core axes: `{"temperature": "Warm", "texture": ["Soft", "Dry"], "light": ["Diffuse"], "atmosphere": ["Muted"]}`
- example expressions: 잎을 으깼을 때 나는 아삭한 초록감처럼 감각의 윤곽이 분명하게 떠오르는 향, 단순한 노트보다 잎을 으깼을 때 나는 아삭한 초록감에 가까운 느낌, 입안과 공기 중에 잎을 으깼을 때 나는 아삭한 초록감의 분위기가 천천히 남는다
- suggested phrase cues: 잎을 으깼을 때 나는 아삭한 초록감, 잎을 으깼을 때 나는 아삭한 초록감, 잎을 으깼을 때 나는 아삭한 초록감 같은 느낌
- negative cues: 과도한 단맛, 무관한 금속성, 탁한 잔향
- related existing objects: green_stem, wet_moss
- similar existing objects: [{"existing_object_id": "wet_moss", "similarity_reason": ["related_existing_object"], "overlap_score": 0.38}, {"existing_object_id": "green_stem", "similarity_reason": ["related_existing_object"], "overlap_score": 0.35}, {"existing_object_id": "cashmere", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "wool_blanket", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "film_grain", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}]

```json
{
  "object_id": "green_leaf_crush",
  "label": "Green Leaf Crush",
  "korean_label": "잎을 으깼을 때 나는 아삭한 초록감",
  "object_type": "sensory_object_draft",
  "family": "Green / Leaf / Crisp",
  "definition": "A crushed green leaf sensation with cool moisture and crisp vegetal snap.",
  "core_axes": {
    "temperature": "Warm",
    "texture": [
      "Soft",
      "Dry"
    ],
    "light": [
      "Diffuse"
    ],
    "atmosphere": [
      "Muted"
    ]
  },
  "example_expressions": [
    "잎을 으깼을 때 나는 아삭한 초록감처럼 감각의 윤곽이 분명하게 떠오르는 향",
    "단순한 노트보다 잎을 으깼을 때 나는 아삭한 초록감에 가까운 느낌",
    "입안과 공기 중에 잎을 으깼을 때 나는 아삭한 초록감의 분위기가 천천히 남는다"
  ],
  "related_objects": [
    "green_stem",
    "wet_moss"
  ],
  "opposite_objects": [],
  "associated_products": [],
  "evidence_refs": [
    "candidate_v1.1"
  ],
  "status": "draft_from_candidate"
}
```

## Needs Distinction Review
- white_musk_clean_skin: similar=[{"existing_object_id": "fresh_linen", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.46}, {"existing_object_id": "clean_room", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.46}, {"existing_object_id": "warm_cotton", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.44}, {"existing_object_id": "after_rain_garden", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}, {"existing_object_id": "green_stem", "similarity_reason": ["axis_overlap"], "overlap_score": 0.07}]
- aldehydic_sparkle: similar=[{"existing_object_id": "clean_room", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.46}, {"existing_object_id": "silver_spoon", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.41}, {"existing_object_id": "fresh_linen", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.11}, {"existing_object_id": "warm_cotton", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}, {"existing_object_id": "after_rain_garden", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}]
- ozonic_air: similar=[{"existing_object_id": "clean_room", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.46}, {"existing_object_id": "cold_fog", "similarity_reason": ["related_existing_object", "family_overlap", "keyword_overlap"], "overlap_score": 0.45}, {"existing_object_id": "fresh_linen", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.11}, {"existing_object_id": "sea_breeze", "similarity_reason": ["family_overlap", "axis_overlap"], "overlap_score": 0.11}, {"existing_object_id": "mountain_stream", "similarity_reason": ["family_overlap"], "overlap_score": 0.09}]
- aquatic_clean_water: similar=[{"existing_object_id": "sea_breeze", "similarity_reason": ["related_existing_object", "family_overlap", "axis_overlap"], "overlap_score": 0.46}, {"existing_object_id": "mountain_stream", "similarity_reason": ["related_existing_object", "family_overlap"], "overlap_score": 0.44}, {"existing_object_id": "fresh_linen", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.11}, {"existing_object_id": "clean_room", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.11}, {"existing_object_id": "cold_fog", "similarity_reason": ["family_overlap", "keyword_overlap"], "overlap_score": 0.1}]
- incense_smoke: similar=[{"existing_object_id": "fireplace_ash", "similarity_reason": ["related_existing_object", "family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.47}, {"existing_object_id": "old_library", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.38}, {"existing_object_id": "dark_resin", "similarity_reason": ["family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.14}, {"existing_object_id": "amber_glow", "similarity_reason": ["family_overlap", "keyword_overlap"], "overlap_score": 0.12}, {"existing_object_id": "dark_chocolate", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}]
- peat_smoke: similar=[{"existing_object_id": "fireplace_ash", "similarity_reason": ["related_existing_object", "family_overlap", "axis_overlap"], "overlap_score": 0.46}, {"existing_object_id": "charred_oak", "similarity_reason": ["related_existing_object", "axis_overlap"], "overlap_score": 0.43}, {"existing_object_id": "forest_floor", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.41}, {"existing_object_id": "dark_chocolate", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "tobacco_leaf", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}]
- oak_tannin_dryness: similar=[{"existing_object_id": "cedarwood", "similarity_reason": ["related_existing_object", "family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.49}, {"existing_object_id": "charred_oak", "similarity_reason": ["related_existing_object", "family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.49}, {"existing_object_id": "black_tea", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.41}, {"existing_object_id": "old_wood", "similarity_reason": ["family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.14}, {"existing_object_id": "cashmere", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}]
- medicinal_smoke: similar=[{"existing_object_id": "fireplace_ash", "similarity_reason": ["related_existing_object", "family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.47}, {"existing_object_id": "cold_metal", "similarity_reason": ["related_existing_object", "keyword_overlap"], "overlap_score": 0.36}, {"existing_object_id": "dark_chocolate", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}, {"existing_object_id": "tobacco_leaf", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}, {"existing_object_id": "charred_oak", "similarity_reason": ["axis_overlap"], "overlap_score": 0.08}]
- clean_finish: similar=[{"existing_object_id": "fresh_linen", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.46}, {"existing_object_id": "clean_room", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.46}, {"existing_object_id": "warm_cotton", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}, {"existing_object_id": "after_rain_garden", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}, {"existing_object_id": "green_stem", "similarity_reason": ["axis_overlap"], "overlap_score": 0.07}]
- mineral_spark: similar=[{"existing_object_id": "wet_stone", "similarity_reason": ["related_existing_object", "family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.52}, {"existing_object_id": "slate", "similarity_reason": ["related_existing_object", "family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.49}, {"existing_object_id": "crystal", "similarity_reason": ["related_existing_object", "family_overlap"], "overlap_score": 0.46}, {"existing_object_id": "granite", "similarity_reason": ["family_overlap", "axis_overlap", "keyword_overlap"], "overlap_score": 0.14}, {"existing_object_id": "marble", "similarity_reason": ["family_overlap", "keyword_overlap"], "overlap_score": 0.12}]
- soap_clean: similar=[{"existing_object_id": "fresh_linen", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.46}, {"existing_object_id": "clean_room", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.46}, {"existing_object_id": "warm_cotton", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}, {"existing_object_id": "after_rain_garden", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}, {"existing_object_id": "green_stem", "similarity_reason": ["axis_overlap"], "overlap_score": 0.07}]
- laundry_musk: similar=[{"existing_object_id": "fresh_linen", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.46}, {"existing_object_id": "clean_room", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.46}, {"existing_object_id": "warm_cotton", "similarity_reason": ["related_existing_object", "axis_overlap", "keyword_overlap"], "overlap_score": 0.44}, {"existing_object_id": "after_rain_garden", "similarity_reason": ["axis_overlap", "keyword_overlap"], "overlap_score": 0.08}, {"existing_object_id": "green_stem", "similarity_reason": ["axis_overlap"], "overlap_score": 0.07}]

## Do Not Merge Yet
- No candidates currently marked do_not_merge_yet.
