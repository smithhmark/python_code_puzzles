
import greatest_subarray

case_1 = [1, 2, 3, -2, 5]
expt_1 = 9
case_2 = [-1, -2, -3, -4,]
expt_2 = -1
case_3 = [5, 7, -3, 2, 9, 6, 16, 22, 21, 29, -14, 10, 12]
expt_3 = 122
case_4 = [ 1,2,3, -10, 5, 4, 3, 2, 1, -20, 1, 2, 3, 4, 5, 6]
expt_4 = 21
case_5 = [-1, -2,1, -3, -4,]
expt_5 = 1

def test_brute():
    assert greatest_subarray.brute(case_1) == expt_1
    assert greatest_subarray.brute(case_2) == expt_2
    assert greatest_subarray.brute(case_3) == expt_3
    assert greatest_subarray.brute(case_4) == expt_4

def test_brute_with_location():
    assert greatest_subarray.brute(case_1, True)[1] == (0, 4)
    assert greatest_subarray.brute(case_4, True)[1] == (10, 15)
    assert greatest_subarray.brute(case_4[:4], True)[1] == (0, 2)
    assert greatest_subarray.brute(case_4[:14], True)[1] == (4, 8)
    assert greatest_subarray.brute(case_2, True)[1] == (0,0)
    assert greatest_subarray.brute(case_5, True)[0] == 1
    assert greatest_subarray.brute(case_5, True)[1] == (2,2)

def test_build_kadane_table():
    tb = greatest_subarray.build_kadane_table(case_1)
    assert tb == [1, 3, 6, 4, 9]
    tb = greatest_subarray.build_kadane_table(case_2)
    assert tb == [-1, -2, -3, -4,]
    tb = greatest_subarray.build_kadane_table(case_3)
    assert tb == [5, 12, 9, 11, 20, 26, 42, 64, 85, 114, 100, 110, 122]
    tb = greatest_subarray.build_kadane_table(case_5)
    assert tb == [-1, -2, 1, -2, -4,]

def test_kadane():
    assert greatest_subarray.kadane(case_1) == expt_1
    assert greatest_subarray.kadane(case_2) == expt_2
    assert greatest_subarray.kadane(case_3) == expt_3
    assert greatest_subarray.kadane(case_4) == expt_4

def test_find_endpoints():
    assert greatest_subarray.find_endpoints(case_1) == (0, 4)
    assert greatest_subarray.find_endpoints(case_4) == (10, 15)
    assert greatest_subarray.find_endpoints(case_4[:4]) == (0, 2)
    assert greatest_subarray.find_endpoints(case_4[:14]) == (4, 8)
    assert greatest_subarray.find_endpoints(case_2) == (0,0)
    assert greatest_subarray.find_endpoints(case_5) == (2,2)
