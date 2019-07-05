import math

import build


case1 = (4, 5, 'aabaacaba')
case2 = (8, 9, 'bacbacacb')
expt1 = 26
expt2 = 42

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

def test_case_simple1():
    assert build.cost_to_build(1,2, "aab") == 3

def test_case_simple2():
    ss = "ab12ab"
    assert build.cost_to_build(2,3, ss) == 11

def test_dp_simple():
    ss = "aab"
    t1 = build.dp_fw(1,2,ss)
    assert max(t1) == 3
    ss = "ab12ab"
    assert build.cost_to_build(2,3, ss) == 11

def test_dp_case1():
    tbl = build.dp_fw(*case1)
    assert max(tbl) == expt1

def test_dp_case2():
    tbl = build.dp_fw(*case2)
    print("final:",tbl)
    print(expt2)
    assert max(tbl) == expt2

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

def test_case1():
    assert build.cost_to_build(*case1) == expt1

def test_case2():
    assert build.cost_to_build(*case2) == expt2

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

def test_dp_case5_0():
    got = build.dp_fw(*case5[0])
    expt = expt5[0]
    print(max(got))
    print(expt)
    assert max(got) == expt

def test_case5_1():
    print(case5[1])
    print(expt5[1])
    got = max(build.dp_fw(*case5[1]))
    expt = expt5[1]
    print(got)
    print(expt)
    assert got == expt

def test_case5_2():
    assert max(build.dp_fw(*case5[2])) == expt5[2]
