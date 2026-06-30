# Axis Evidence & Clarification Layer v1.3

## 목적

Axis Evidence & Clarification Layer는 parser output의 해석 가능성을 높이기 위한 레이어입니다. Sensory Atlas가 어떤 감각 축을 왜 추론했는지, 어떤 표현이 근거로 쓰였는지, 그리고 해석이 애매할 때 사용자에게 무엇을 되물어야 하는지를 보여줍니다.

## 왜 필요한가

전체 confidence 하나만으로는 감각 표현의 해석 과정을 충분히 설명하기 어렵습니다. 사용자의 은유적 감각 언어는 온도감, 질감, 빛, 분위기, 움직임, 렌더링 방식을 동시에 섞는 경우가 많습니다.

축별 evidence와 confidence를 분리하면 사용자는 parser가 어떤 축에서는 강한 근거를 가졌고, 어떤 축에서는 약한 근거로 추론했는지 확인할 수 있습니다. 이는 Sensory Atlas를 단순 추천기가 아니라 감각 언어 구조화 시스템으로 유지하는 데 중요합니다.

## axis_evidence

`axis_evidence`는 각 sensory axis를 추론할 때 입력 문장에서 감지된 근거 표현을 담습니다.

주요 근거는 다음에서 수집됩니다.

- matched sensory descriptors
- phrase cues
- activated cue groups
- descriptor layer support

예시:

```json
{
  "temperature": ["차가운", "서늘한"],
  "texture": ["축축한", "젖은"],
  "atmosphere": ["숲", "비 온 뒤"]
}
```

현재 구현은 완전한 형태소 분석이 아니라 substring과 descriptor 기반의 rule-based matching입니다.

## axis_confidence

`axis_confidence`는 각 축에 대한 근거 강도를 0.0에서 1.0 사이의 값으로 표현합니다.

axis_confidence는 학습된 확률값이 아니라, 현재 rule-based parser가 해당 축을 얼마나 강한 근거로 추론했는지를 나타내는 heuristic evidence-strength score입니다.

현재 점수는 다음 요소를 단순 조합합니다.

- evidence item 개수
- cue hierarchy support 여부
- inferred axis value 존재 여부

따라서 이 값은 모델의 통계적 확률이나 정답 가능성이 아니라, parser 내부 근거의 상대적 강도로 읽어야 합니다.

## clarification_questions

`clarification_questions`는 low-confidence 또는 ambiguous output에 대해 생성되는 사용자 확인 질문입니다.

이 질문은 제품 추천을 위한 질문이 아니라, 사용자의 감각 표현을 더 정확히 구조화하기 위한 질문입니다.

예시:

```text
이 표현은 더 차갑고 선명한 느낌인가요, 아니면 따뜻하고 포근한 느낌인가요?
질감은 더 보송한 쪽인가요, 축축한 쪽인가요, 매끈한 쪽인가요?
분위기는 더 자연적이고 숲에 가까운가요, 도시적이고 인공적인 쪽인가요?
```

질문은 최대 3개까지 생성되며, 입력이 충분히 명확한 경우 비어 있을 수 있습니다.

## 한계

- 아직 rule-based parser입니다.
- evidence extraction은 substring/descriptor 기반입니다.
- confidence는 heuristic evidence-strength score입니다.
- clarification question은 template 기반입니다.
- 사용자 답변을 다시 parser output에 반영하는 interactive loop는 아직 구현되지 않았습니다.

## 다음 단계

- clarification answer를 parser output refinement에 반영
- 사용자 feedback case 저장
- modifier group을 object ranking constraint에 연결
- candidate sensory object review workflow를 v1.4에서 추가
