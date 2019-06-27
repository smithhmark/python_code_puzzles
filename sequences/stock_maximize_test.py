
import stock_maximize


case_1 = [5, 3, 2]
case_2 = [1, 2, 100]
case_3 = [1, 3, 1, 2]
expt_1 = 0
expt_2 = 197
expt_3 = 3


def test_brute():
    assert stock_maximize.brute(case_1) == expt_1
    assert stock_maximize.brute(case_2) == expt_2
    assert stock_maximize.brute(case_3) == expt_3

def test_clever():
    assert stock_maximize.clever(case_1) == expt_1
    assert stock_maximize.clever(case_2) == expt_2
    assert stock_maximize.clever(case_3) == expt_3

def test_clever_get_trades():
    a, b =stock_maximize.clever(case_1, True)
    assert a == expt_1
    assert sorted(b) == sorted([])
    
    a, b =stock_maximize.clever(case_2, True)
    assert a == expt_2
    assert sorted(b) == sorted([(0,2), (1,2)])
