
import grid_traverse

def test_build_table():
    tbl = grid_traverse.build_table(3,2)
    assert len(tbl) == 3
    assert len(tbl[0]) == 2
    #print(grid_traverse.stringify_table(tbl))
    #assert False

def test_stringify():
    tbl = [[0,0],[0,0]]
    ss = grid_traverse.stringify_table(tbl)
    assert ss == "0,0\n0,0"

def test_three_by_three():
    tbl = grid_traverse.build_table(3,3)
    print(grid_traverse.stringify_table(tbl))
    #assert False

