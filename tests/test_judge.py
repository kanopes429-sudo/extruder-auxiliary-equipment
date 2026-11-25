"""판정 함수 테스트. 요구사항 표(docs/requirements.md)의 숫자를 그대로 확인한다."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from judge import judge


def good_result():
    """모든 항목을 통과하는 기준 결과"""
    return {
        "placed_in_order": 6,
        "dropped": 0,
        "max_time_per_plate": 35.0,
        "moves_in_protect_zone": 0,
        "early_unbolt_signal": 0,
        "early_pull": 0,
    }


def test_all_pass():
    assert judge(good_result())["pass"] is True


def test_r01_fails_when_plate_missing():
    r = good_result()
    r["placed_in_order"] = 5
    out = judge(r)
    assert out["R-01"] is False
    assert out["pass"] is False


def test_r02_fails_when_dropped():
    r = good_result()
    r["dropped"] = 1
    assert judge(r)["R-02"] is False


def test_r03_boundary():
    r = good_result()
    r["max_time_per_plate"] = 40.0   # 경계값은 통과
    assert judge(r)["R-03"] is True
    r["max_time_per_plate"] = 40.1
    assert judge(r)["R-03"] is False


def test_safety_fails_on_any_violation():
    for key in ["moves_in_protect_zone", "early_unbolt_signal", "early_pull"]:
        r = good_result()
        r[key] = 1
        out = judge(r)
        assert out["safety"] is False, key
        assert out["pass"] is False, key
