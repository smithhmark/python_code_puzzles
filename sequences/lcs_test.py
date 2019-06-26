import lcs

case_1 = ("ABCDGH", "AEDFHR")
expt_1 = "ADH"
case_2 = ("AGGTAB", "GXTXAYB")
expt_2 = "GTAB"

def test_binaray_width():
    assert lcs.binary_width(8) == 4
    assert lcs.binary_width(7) == 3
    assert lcs.binary_width(1) == 1
    assert lcs.binary_width(0) == 1

def test_binary_1s():
    assert lcs.binary_1s(3) == [0,1]
    assert lcs.binary_1s(8) == [0]
    assert lcs.binary_1s(7) == [0,1,2]
    assert lcs.binary_1s(1) == [0]
    assert lcs.binary_1s(0) == []

def test_powerset():
    assert lcs.powerset([]) == [[]]
    assert sorted(lcs.powerset([1])) == sorted([[], [1], ])
    assert sorted(lcs.powerset([1,2])) == sorted([[], [1], [2], [1,2]])

def test_powerset_of_strings():
    assert lcs.powerset_str("") == [""]
    assert sorted(lcs.powerset_str("1")) == sorted(["", "1", ])
    assert sorted(lcs.powerset_str("12")) == sorted(["", "1", "2", "12"])

def test_brute():
    assert lcs.brute(case_1[0], case_1[1])[1] == expt_1
    assert lcs.brute(case_2[0], case_2[1])[1] == expt_2

def test_stringify_table():
    assert lcs.stringify_table([[0,0],[0,0]]) == "0,0\n0,0"

def test_build_dp_table_hiho():
    tab = lcs.build_dp_table("hi", "ho")
    assert len(tab) == 3
    assert len(tab[0]) == 3

    for row in tab:
        assert row[0] == 0
    for col in tab[0]:
        assert col == 0
    assert tab[1][1] == 1
    #print(lcs.stringify_table(tab))
    #assert False

def test_build_dp_table_abxy():
    tab = lcs.build_dp_table("ab", "xy")
    assert len(tab) == 3
    assert len(tab[0]) == 3

    for row in tab:
        assert row[0] == 0
    for col in tab[0]:
        assert col == 0
    assert tab[1][1] == 0
    #print(lcs.stringify_table(tab))
    #assert False

def test_build_dp_table_case1():
    #case_1 = ("ABCDGH", "AEDFHR")
    tab = lcs.build_dp_table(case_1[0], case_1[1])
    #print(lcs.stringify_table(tab))
    for row in tab:
        assert row[0] == 0
    for col in tab[0]:
        assert col == 0
    assert tab[1][1] == 1
    assert tab[-1][-1] == 3

def test_lcs_length():
    s1, s2 = case_1
    assert lcs.length_dp(s1, s2) == len(expt_1)
    s1, s2 = case_2
    assert lcs.length_dp(s1, s2) == len(expt_2)

def test_lcs_dp():
    s1, s2 = case_1
    a, b =lcs.lcs_dp(s1, s2)
    assert a == b
    assert "".join(a) == expt_1

