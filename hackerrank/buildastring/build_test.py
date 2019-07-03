
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

def test_case_simple():
    assert build.cost_to_build(1,2, "aab") == 3
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
    assert build.cost_to_build(*case3[1]) == expt3[1]
def test_case3_2():
    assert build.cost_to_build(*case3[2]) == expt3[2]
