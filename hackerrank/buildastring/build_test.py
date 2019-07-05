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
    assert build.cost_forward(1,2, "aab") == build.cost_backward(1,2, "aab")

def test_case_simple2():
    ss = "ab12ab"
    print_workup_hort(2,3, ss)
    print(build.stringify_table(build.forward_table(2,3,ss), ss))
    print(build.stringify_table(build.backward_table(2,3,ss), ss))
    assert build.cost_to_build(2,3, ss) == 11
    assert build.cost_backward(2,3, ss) == build.cost_forward(2,3, ss)

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

def test_interpret_fw():
    t = build.forward_table(2,3, "ab12ab")
    assert build.interpret_ft(t, 2,3) == list("aaaabb")

def test_interpret_bw():
    s = "ab12ab"
    t = build.backward_table(2,3, s)
    print(build.stringify_table(t,s))
    assert build.interpret_bt(t,2,3) == list("aaaabb")

def test_case1():
    assert build.cost_to_build(*case1) == expt1
    assert build.cost_backward(*case1) == build.cost_forward(*case1)

def test_case2():
    assert build.cost_backward(1,2,case2[2]) == build.cost_forward(1,2,case2[2])
    assert build.cost_backward(*case2) == build.cost_forward(*case2)
    assert build.cost_to_build(*case2) == expt2

def test_case3_0():
    assert build.cost_to_build(*case3[0]) == expt3[0]
    assert build.cost_backward(*case3[0]) == build.cost_forward(*case3[0])

def test_case3_1():
    assert build.cost_backward(*case3[1]) == build.cost_forward(*case3[1])
    print(case3[1])
    got = build.cost_to_build(*case3[1])
    expt = expt3[1]
    print(got)
    print(expt)
    assert got == expt

def test_case3_2():
    assert build.cost_backward(*case3[2]) == build.cost_forward(*case3[2])
    assert build.cost_to_build(*case3[2]) == expt3[2]

def print_workup_hort(a,b,s, width=60):
    ft = build.forward_table(a,b,s)
    bt = build.backward_table(a,b,s)
    fs = build.interpret_ft(ft, a, b)
    bs = build.interpret_bt(bt, a, b)
    d = build.compare_tis(fs, bs)
    windows = math.ceil(len(s)/width)
    for window in range(windows):
        print("w:", window)
        print("".join(d[width*window:width*(window+1)]))
        print(s[width*window:width*(window+1)])
        print("".join(fs[width*window:width*(window+1)]))
        print("".join(bs[width*window:width*(window+1)]))

def print_workup_vert(a,b,s):
    ft = build.forward_table(a,b,s)
    bt = build.backward_table(a,b,s)
    fs = build.interpret_ft(ft, a, b)
    bs = build.interpret_bt(bt, a, b)
    d = build.compare_tis(fs, bs)
    for ln in zip(fs, d, bs, s):
        print("{}:{}:{}\t{}".format(*ln))

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
