
def kangaroo(x1, v1, x2, v2):
    # x1 + i * v1 ?= x2 + i * v2
    # x1 - x2 =? i(v2 - v1)
    # (x1 -x1)/(v2-v1) = i, where i >=1, is int, and x1 + v1*i <= 100000
    x_diff = x1-x2
    v_diff = v2 - v1
    if v_diff == 0:
        return None
    jumps = x_diff / v_diff
    if jumps >= 1 and jumps.is_integer():
        assert x1 + jumps * v1 == x2 + jumps * v2
        return jumps
    return None

def dumb(x1,x2,v1,v2, N):
    for jump in range(N):
        k1 = x1 + jumps * v1
        k2 = x2 + jumps * v2
        if k1 == k2:
            return jumps

def exhaust(N):
    for x1 in range(N):
        for x2 in range(x1+1, N+1):
            for v1 in range(1,N+1):
                for v2 in range(1,N+1):
                    try:
                        kangaroo(x1,x2,v1,v2)
                    except RuntimeError as e:
                        print(e)
                        print(x1,x2,v1,v2)
exhaust(100)

