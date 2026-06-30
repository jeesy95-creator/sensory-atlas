# General Sensory Vocabulary Layer v1.2

## 목적

General Sensory Vocabulary Layer는 domain-specific vocabulary보다 더 낮은 수준의 일반 감각 descriptor를 구조화하기 위한 레이어다. 향수의 `bergamot`, 위스키의 `peat smoke`, 와인의 `tannin` 같은 도메인 용어가 “무엇을 말하는지”를 설명한다면, 일반 감각 어휘는 그 감각이 “어떻게 느껴지는지”를 설명한다.

예를 들어 `차갑다`, `부드럽다`, `맑다`, `무겁다`, `퍼지다`, `잔상이 남다`, `윤이 나다` 같은 표현은 보통 sensory object가 아니다. 이들은 temperature, texture, clarity, density, motion, finish, rendering 같은 축을 조정하거나 object ranking을 제약하는 descriptor다.

## 핵심 원칙

1. 이 프로젝트는 향수/위스키 추천기가 아니라 감각 언어 구조화 프로젝트다.
2. 새로운 단어를 바로 sensory object로 넣지 않는다.
3. 일반 형용사와 부사는 object가 아니라 axis descriptor나 modifier로 둔다.
4. 도메인 vocabulary는 candidate layer에 먼저 쌓고, 검토 후 main ontology에 병합한다.
5. parser 성능을 올리기 위해 holdout 문장을 직접 cue로 복사하지 않는다.
6. 데이터 확장은 example, phrase cue, modifier, mapping, candidate를 구분해서 진행한다.
7. parser logic 변경은 데이터 레이어로 해결이 안 될 때만 한다.
8. 성능 지표는 항상 default, blind, holdout을 분리해서 본다.

## 왜 필요한가

Domain vocabulary는 `bergamot`, `peat smoke`, `tannin`처럼 특정 domain에서 자주 쓰이는 note, accord, tasting descriptor를 설명한다. 하지만 사용자는 훨씬 일반적인 감각 언어로 말한다.

```text
차갑고 맑다
부드럽게 감싼다
낮게 깔린다
처음엔 선명하고 뒤로 갈수록 둥글다
필름처럼 잔상이 남는다
```

이런 표현은 특정 재료명보다 감각의 shape, movement, finish, clarity를 더 잘 설명한다. v1.2는 이 일반 감각 어휘를 별도 데이터 레이어로 모아 향후 parser scoring, axis update, modifier group, expression pattern rule에 사용할 수 있게 한다.

## 데이터 구조

### `data/general_sensory_vocabulary.csv`

일반 감각 어휘를 row 단위로 정리한 CSV다. 각 row는 term, 품사, primary axis, descriptor type, polarity, intensity, synonym group, opposite terms, example phrases, related objects, integration status를 포함한다.

### `data/sensory_axis_descriptors.json`

temperature, texture, density, light, clarity, motion, time, finish, space, atmosphere, shape, edge, moisture, organic, mineral, rendering, balance 축별 descriptor group을 정의한다. 각 축은 최소 5개 이상의 descriptor group을 가진다.

### `data/sensory_modifier_groups.json`

여러 축이 결합된 modifier group을 정의한다. 예를 들어 `cold_clear`, `wet_green`, `dry_smoky`, `film_like_mood`, `skin_like_softness` 같은 group은 object가 아니라 향후 ranking constraint 또는 axis modifier로 사용할 후보다.

### `data/sensory_expression_patterns.jsonl`

한국어 감각 표현의 일반 pattern을 모은 JSONL 파일이다. `A지만 B는 아니다`, `처음엔 A, 뒤로 갈수록 B`, `A보다는 B에 가깝다` 같은 표현은 향후 parser가 clause 간 관계를 이해하는 데 필요하다.

## Sensory Object와 Axis Descriptor의 차이

`차갑다`, `부드럽다`, `맑다`는 그 자체로 sensory object가 아니다. 이런 표현은 object를 활성화하기보다 axis score를 조정하거나 object ranking을 제약해야 한다.

```text
차갑다 → temperature axis
차갑고 투명하다 → cold_clear modifier group
차갑고 투명하고 단단하다 → crystal / cut_diamond / cold_metal candidate objects
```

즉, descriptor는 감각 object의 후보를 좁히는 조건으로 작동해야지 main ontology에 무분별하게 추가되어서는 안 된다.

## Modifier Group 예시

```text
cold_clear → crystal / cut_diamond / winter_dawn 계열과 가까움
warm_soft → cashmere / warm_cotton / wool_blanket 계열과 가까움
wet_green → wet_moss / green_stem / after_rain_garden 계열과 가까움
dry_smoky → fireplace_ash / charred_oak / tobacco_leaf 계열과 가까움
film_like_mood → film_grain / old_library / late_night_air 계열과 가까움
four_k_precision → four_k_clarity / cut_diamond / crystal 계열과 가까움
skin_like_softness → warm_cotton / cashmere / leather 계열과 가까움
```

## Expression Pattern 예시

```text
A지만 B는 아니다
처음엔 A, 뒤로 갈수록 B
A보다는 B에 가깝다
A가 얇게 퍼진다
A가 낮게 깔린다
A와 B 사이
```

이 pattern들은 v1.2에서 parser에 연결하지 않는다. 대신 향후 rule refinement나 LLM-assisted parser fallback에서 사용할 수 있는 후보 규칙으로 보관한다.

## 저작권 / 데이터 사용 원칙

- 이 레이어는 원본 한국어 감각 표현으로 작성한 curated vocabulary resource다.
- 리뷰 문장, 제품 설명, 유료 데이터베이스 문구를 복사하지 않는다.
- 일반적으로 쓰이는 감각 개념만 참고하고, example phrase는 새로 작성한다.
- holdout 문장을 그대로 cue나 pattern으로 복사하지 않는다.

## 다음 단계

- general descriptor를 parser scoring에 soft constraint로 연결한다.
- modifier group을 object ranking 보정에 사용한다.
- expression pattern을 clause-level parsing rule로 발전시킨다.
- user feedback case를 추가한다.
- embedding fallback 또는 LLM-assisted parser를 같은 schema 뒤에 연결한다.
- domain-specific demo mode에서 domain vocabulary와 general descriptor를 함께 보여준다.
