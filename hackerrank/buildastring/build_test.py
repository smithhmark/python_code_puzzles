import math
import pytest

import build


case0 = [(4, 5, 'aabaacaba'),
         (8, 9, 'bacbacacb'),
         ]
expt0 = [26,42]

case1 = [(2, 3, "caaahqcqes"),
        (1, 3, "acbbqbbqbb"),
        (2, 4, "cbabecbahe")]    
expt1 = [20, 10, 18,]

case3 = [
    (1, 2, "cbaasgcbiikaegcbiidcbaasgcbiikaegcbiidir"),
    (1, 3, "cabcjpsdaedsasedsascabcjpsddsdaedsasedsa"),
    (2, 3, "cbacojcrojcrlidickjcjcrojcrlijcrojcrrojq"),
    ]
expt3 = [ 20, 24, 45,]
case5 = [
    (2709, 2712, 'caackncaacknggikncaacknggaacknggikncaackggikncaacknggaacknggikncakqoaacknggikncacggihikncaomhikncaom'),
    (7890, 7891, 'acbcrsjcrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcrsjrscrsjcrcbcrsjcrscrsjccbcrsjcrscrsjcrcbcsbcbcrsjh'),
    (7078, 7078, 'abbciabbcabciabbcmabbciabbcahlbchgcmabbcmggcmababciabbcagerafrciabbcsrhgcmcabciabbchgcmabbcmsfabcmsr')
    ]
expt5=[65040, 126246, 268964, ]

case7_path = './input07.txt'
expt7 = [107176, 471776, 2607120 ]

case11_path = './input11.txt'
expt11 = [400809, 729904, 32225646]

@pytest.fixture
def test11_cases():
    cases = load_cases(case11_path)
    return list(zip(cases, expt11))

def load_cases(path):
    cases = []
    with open(path, "r") as ifil:
        cnt = int(ifil.readline())
        for _ in range(cnt):
            [lenth, a, b] = list(map(int, ifil.readline().split()))
            target = ifil.readline().strip()
            if len(target) != lenth:
                print("ut oh")
            else:
                cases.append((a, b, target))
    return cases

def test_case_simple1():
    assert build.cost_to_build(1,2, "aab") == 3

def test_recursive_simple1():
    assert build.recursive(1,2, "aab") == 3

def test_find_longest_ending_here():
    target = case0[0][-1]
    matched, whr = build._find_longest_ending_here(target, 0)
    assert matched is None
    matched, whr = build._find_longest_ending_here(target, 4)
    assert matched == "aa"
    assert whr == 0

    target = case0[1][-1]
    matched, whr = build._find_longest_ending_here(target, 0)
    assert matched is None
    matched, whr = build._find_longest_ending_here(target, 5)
    assert matched == "bac"
    assert whr == 0

def test_case_simple2():
    ss = "ab12ab"
    assert build.cost_to_build(2,3, ss) == 11

def test_recursive_case_simple2():
    ss = "ab12ab"
    assert build.recursive(2,3, ss) == 11
def test_scan_for_prefix():
    target = case0[0][-1]
    jumps, prefs, prevs = build.scan_for_prefix(target)
    print(target)
    print(prefs)
    print(jumps)
    print(prevs)
    #assert False

def test_dp_simple0():
    ss = "aab"
    t1 = build.dp_fw(1,2,ss)
    print(t1)
    assert max(t1) == 3
    ss = "ab12ab"
    assert max(build.dp_fw(2,3, ss)) == 11

def test_case0_0():
    print(case0[0])
    assert build.cost_to_build(*case0[0]) == expt0[0]

def test_case0_1():
    print(case0[1])
    assert build.cost_to_build(*case0[1]) == expt0[1]

def test_case1_0():
    assert build.cost_to_build(*case1[0]) == expt1[0]
def test_case1_1():
    assert build.cost_to_build(*case1[1]) == expt1[1]

def test_case7():
    cases = load_cases(case7_path)
    for case, expt in zip(cases, expt7):
        print(case)
        print(expt)
        assert build.cost_to_build(*case) == expt

@pytest.mark.skip
def test_case11_0(test11_cases):
    case, expt = test11_cases[0]
    print(case)
    print(expt)
    assert build.cost_to_build(*case) == expt

def test_case11_1(test11_cases):
    case, expt = test11_cases[1]
    print(case)
    print(expt)
    assert build.cost_to_build(*case) == expt

def test_case11_2(test11_cases):
    case, expt = test11_cases[2]
    print(case)
    print(expt)
    assert build.cost_to_build(*case) == expt

def test_dp_case0_0():
    tbl = build.dp_fw(*case0[0])
    assert max(tbl) == expt0[0]

def test_dp_case0_1():
    tbl = build.dp_fw(*case0[1])
    print("final:",tbl)
    print(expt0[1])
    assert max(tbl) == expt0[1]

def test_dp_case1_0():
    tbl = build.dp_fw(*case1[0])
    print(case1[0])
    print(tbl)
    assert max(tbl) == expt1[0]

def test_dp_case1_1():
    tbl = build.dp_fw(*case1[1])
    print(case1[1])
    print(tbl)
    assert max(tbl) == expt1[1]

def test_dp_case1_2():
    tbl = build.dp_fw(*case1[2])
    print(case1[2])
    print(tbl)
    assert max(tbl) == expt1[2]

def test_dp_case3_0():
    tbl = build.dp_fw(*case3[0])
    print("final:",tbl)
    print(expt3[0])
    assert max(tbl) == expt3[0]

def test_dp_case3_1():
    tbl = build.dp_fw(*case3[1])
    print("final:",tbl)
    print(expt3[1])
    assert max(tbl) == expt3[1]

def test_dp_case3_2():
    tbl = build.dp_fw(*case3[2])
    print("final:",tbl)
    print(expt3[2])
    assert max(tbl) == expt3[2]

def test_case3_0():
    assert build.cost_to_build(*case3[0]) == expt3[0]

def test_case3_1():
    print(case3[1])
    got = build.cost_to_build(*case3[1])
    expt = expt3[1]
    print(got)
    print(expt)
    assert got == expt
def test_case3_2():
    assert build.cost_to_build(*case3[2]) == expt3[2]

def test_case5_0():
    assert build.cost_to_build(*case5[0]) == expt5[0]
def test_case5_1():
    assert build.cost_to_build(*case5[1]) == expt5[1]
def test_case5_2():
    assert build.cost_to_build(*case5[2]) == expt5[2]

def test_dp_case5_0():
    got = build.dp_fw(*case5[0])
    expt = expt5[0]
    print(max(got))
    print(expt)
    assert max(got) == expt

def test_dp_case5_1():
    print(case5[1])
    print(expt5[1])
    got = max(build.dp_fw(*case5[1]))
    expt = expt5[1]
    print(got)
    print(expt)
    assert got == expt

def test_dp_case5_2():
    assert max(build.dp_fw(*case5[2])) == expt5[2]
