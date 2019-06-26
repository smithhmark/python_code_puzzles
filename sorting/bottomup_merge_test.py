
import bottomup_merge as merge

def test_merge_params_len2():
    window = 0
    sorted_len = 1
    arry_sz = 2

    start, mid, end = merge.merge_params(sorted_len, arry_sz, window)
    assert start == 0
    assert mid == 0
    assert end == 1

def test_merge_params_len2_win1():
    window = 1
    sorted_len = 1
    arry_sz = 4

    start, mid, end = merge.merge_params(sorted_len, arry_sz, window)
    assert start == 2
    assert mid == 2
    assert end == 3

def test_merge_params_len3():
    window = 0
    sorted_len = 1
    arry_sz = 3

    start, mid, end = merge.merge_params(sorted_len, arry_sz, window)
    assert start == 0
    assert mid == 0
    assert end == 1

    window = 1
    start, mid, end = merge.merge_params(sorted_len, arry_sz, window)
    assert start == 2
    assert mid == 2
    assert end == 2


def test_merge_params_len4():
    window = 0
    sorted_len = 2
    arry_sz = 4

    start, mid, end = merge.merge_params(sorted_len, arry_sz, window)
    assert start == 0
    assert mid == 1
    assert end == 3

def test_merge_1digit_inorder():
    data = [1,2]
    tmp = [0] * 2
    merge.merge(data, tmp, 0, 0, 1)
    assert tmp == data

def test_merge_1digit_reversed():
    data = [2,1]
    tmp = [0] * 2
    merge.merge(data, tmp, 0, 0, 1)
    assert tmp == [1,2]

def test_merge_case1():
    data = [1,2,3,4]
    tmp = [0] * 4
    merge.merge(data, tmp, 0, 1, 3)
    assert tmp == data

    data2 = [3, 4, 1,2,]
    tmp = [0] * 4
    merge.merge(data2, tmp, 0, 1, 3)
    assert tmp == data

def test_sort_len3():
    data = list(range(3, 0, -1))
    expt = sorted(data)
    print(data)

    rcvd = merge.sort(data)
    assert rcvd == expt

def test_sort_len30():
    data = list(range(30, 0, -1))
    expt = sorted(data)
    print(data)

    rcvd = merge.sort(data)
    assert rcvd == expt

def test_counting_sort():
    data = [1, 2, 4, 3, 5]
    expt = sorted(data)
    print(data)
    srtd, cnts = merge.counting_sort(data)
    print(cnts)
    assert srtd == expt
    assert cnts[1] == 0
    assert cnts[2] == 0
    assert cnts[3] == 0
    assert cnts[4] == 1
    assert cnts[5] == 0

    data = [1, 4, 3, 2, 5]
    expt = sorted(data)
    print(data)
    srtd, cnts = merge.counting_sort(data)
    print(cnts)
    assert srtd == expt
    assert cnts[1] == 0
    assert cnts[2] == 0
    assert cnts[3] == 1
    assert cnts[4] == 2
    assert cnts[5] == 0
