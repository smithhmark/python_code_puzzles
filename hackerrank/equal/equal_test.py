import equal


example_rounds = [1,2,5]
case1 = [2,2,3,7]
expt1 = 2

case2 = [10, 7, 12]
expt2 = 3

case11 = [1, 5, 5]
expt11 = 3

case12 = [1, 5, 5, 10, 10]
expt12 = 7

case15_path = './input15.txt'
expt15_path = './output15.txt'

def test_find_first_gap():
    assert equal.find_first_gap(case1) == 2
    assert equal.find_first_gap(case2) == 2
    assert equal.find_first_gap([1,1,1,1]) == -1
    assert equal.find_first_gap([1]) == -1

def test_rounds_between():
    assert equal.rounds_between(2,3) == 1
    assert equal.rounds_between(0, 7) == 2
    assert equal.rounds_between(0, 7) == 2
    assert equal.rounds_between(7, 7) == 0
    assert equal.rounds_between(0, 7, [9]) == -1

def test_build_diffs():
    assert equal.build_differences(case1) == [0, 1, 4]
    tmp = sorted(case2)
    assert equal.build_differences(tmp) == [3,2]

def test_build_table_down():
    tab = equal._build_table_down(case1, example_rounds)
    print(tab)
    assert tab[0] == 2
    assert tab[1] == 5
    tab = equal._build_table_down(case2, example_rounds)
    print(tab)
    assert tab[0] == 3
    assert tab[1] == 5
    tab = equal._build_table_down(case11, example_rounds)
    print(tab)
    assert tab[0] == 4
    assert tab[1] == 3

def test_min_rounds():
    assert equal.min_rounds(case1, example_rounds) == expt1
    assert equal.min_rounds(case2, example_rounds) == expt2

def test_min_rounds_failed():
    assert equal.min_rounds(case11, example_rounds) == expt11
    assert equal.min_rounds(case12, example_rounds) == expt12

def test_adapted():
    assert equal.find_min_actions(case11) == expt11
    assert equal.find_min_actions(case12) == expt12

def load_case15():
    expts = []
    with open(expt15_path, "r") as ifil:
        for line in ifil:
            expts.append(int(line.strip()))

    cases = []
    with open(case15_path, "r") as ifil:
        case_cnt = int(ifil.readline())
        if case_cnt != len(expts):
            print("oh no, don't have the same numbers for results as tests")
            return None, None
        for test in range(case_cnt):
            N = int(ifil.readline().strip())
            arr = list(map(int, ifil.readline().split()))
            if len(arr) != N:
                print("error in case{}".format(N))
            cases.append(arr)
    return expts, cases

def test_case15_1():
    expts, cases = load_case15()
    print("expect:", expts[1])
    #print(cases[1])
    ns = list(sorted(cases[1]))
    print("ns[:15]:",ns[:15])
    print("ns[-15]:",ns[-15:])
    expt = expts[1]
    dp = equal._build_table_down(ns, [1,2,5])
    print("dp:",dp)
    got = equal.min_rounds(ns)
    print("got:",got)
    assert got == expt

def test_all_case15():
    expts, cases = load_case15()
    assert len(expts) == len(cases)
    fails = []
    #for ii, result in enumerate(expts[:10]):
    for ii, result in enumerate(expts):
        #print("trying case:",ii)
        got =equal.min_rounds(cases[ii])
        #got = equal.find_min_actions(cases[ii])
        if result != got:
            fails.append((ii, got - result))
    print(fails)
    assert len(fails) == 0
