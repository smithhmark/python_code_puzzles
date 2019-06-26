
import greatestspan

tricky_val = [5,10,0,1,2,3,4]

def test_simplest():
    vals = [ 34, 8, 10, 3, 2, 80, 30, 33, 1]
    expt = 6 # idx 8 - idx 1
    assert greatestspan.simplest(vals) == expt

def test_simplest_tricky():
    assert greatestspan.simplest(tricky_val) == 4

def test_linear():
    vals = [ 34, 8, 10, 3, 2, 80, 30, 33, 1]
    expt = 6 # idx 8 - idx 1

    assert greatestspan.linear(vals) == expt

def test_linear_tricky():
    assert greatestspan.linear(tricky_val) == 4
