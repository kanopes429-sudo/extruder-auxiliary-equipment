"""한 판(판 6장 처리) 결과를 받아 요구사항 통과 여부를 판정한다.

관련: docs/requirements.md  R-01, R-02, R-03(Must), R-04, R-06, R-07(안전)
"""

PLATE_COUNT = 6           # R-01 판 장수
MAX_TIME_PER_PLATE = 40.0 # R-03 판당 시간 상한 (s)


def judge(result: dict) -> dict:
    """result를 받아 항목별 통과 여부를 돌려준다.

    result 키:
        placed_in_order       순서대로 놓인 판 수 (개)
        dropped               낙하 수 (개)
        max_time_per_plate    판당 걸린 시간 중 최댓값 (s)
        moves_in_protect_zone 보호 구역 안 팔 이동 횟수 (회)
        early_unbolt_signal   핀 체결 전 해체 신호 횟수 (회)
        early_pull            분리 완료 전 빼내기 횟수 (회)
    """
    r01 = result["placed_in_order"] == PLATE_COUNT
    r02 = result["dropped"] == 0
    r03 = result["max_time_per_plate"] <= MAX_TIME_PER_PLATE
    safety = (
        result["moves_in_protect_zone"] == 0
        and result["early_unbolt_signal"] == 0
        and result["early_pull"] == 0
    )
    return {
        "R-01": r01,
        "R-02": r02,
        "R-03": r03,
        "safety": safety,
        "pass": r01 and r02 and r03 and safety,
    }
