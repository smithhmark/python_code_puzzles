import coin_change

case1 = (4, [ 1, 2, 3])
expt1 = 4
case2 = (10, [ 2, 5, 3, 6,])
expt2 = 5

def test_dp():
    ways = coin_change.build_dp(case1[0], case1[1])
    assert ways == expt1
    ways = coin_change.build_dp(case2[0], case2[1])
    assert ways == expt2
