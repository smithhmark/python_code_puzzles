import between_two_sets

case_1_a = [2,6]
case_1_b = [24, 36]
expt_1 = [6,12]

case_2_a = [2,4]
case_2_b = [16, 32, 96]
expt_2 = 3

def test_factor():
    assert between_two_sets.factor(4) == [4, 2]
    assert between_two_sets.factor(3) == [3]
    assert between_two_sets.factor(5) == [5]
    assert between_two_sets.factor(12) == [12,6,4,3,2]

def test_get_betweens_1():
    got =between_two_sets.get_betweens(case_1_a, case_1_b)
    assert got == set(expt_1)

def test_get_betweens_2():
    got =between_two_sets.get_betweens(case_2_a, case_2_b)
    assert len(got) == expt_2
