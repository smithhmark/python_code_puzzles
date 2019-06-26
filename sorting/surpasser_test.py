
import surpasser

def test_case1():
    given = [2, 7, 5, 3, 0, 8, 1, ]
    expect = [4, 1, 1, 1, 2, 0, 0,]
    
    got = surpasser.get_counts(given)
    assert got == expect

def test_brute_case1():
    given = [2, 7, 5, 3, 0, 8, 1, ]
    expect = [4, 1, 1, 1, 2, 0, 0,]
    
    got = surpasser.brute(given)
    assert got == expect
