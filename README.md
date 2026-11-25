# extruder-auxiliary-equipment

압출 금형 판 교체를 돕는 협동 로봇팔 MuJoCo 시뮬레이션

- 사용자: 특수 형상 플라스틱 압출 라인 작업자
- 문제: 200\~300℃로 가열된 금형 판(최대 약 20kg)을 사람이 받치고 옮긴다. 화상·낙하·허리 부상 위험
- 로봇: UR10e + Robotiq 2F-85 + 잠금 핀 장치 (MuJoCo Menagerie)
- 범위: 판 6장을 순서대로 붙잡고, 사람이 분리하면 빼내어 바닥 구역에 내려놓는다

## 폴더

| 폴더 | 내용 |
|---|---|
| `docs/` | 산출물 문서 (charter, register, problem, requirements …) |
| `scenes/` | MuJoCo 장면 XML |
| `src/` | 로봇 프로그램 |
| `tests/` | 판정 테스트 |
| `logs/` | 실행 기록 |

## 실행

```bash
uv sync
uv run pytest
uv run python -m mujoco.viewer --mjcf=scenes/<장면>.xml
```
