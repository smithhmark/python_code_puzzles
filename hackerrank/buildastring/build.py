
"""
https://www.hackerrank.com/challenges/build-a-string/problem


"""
import math

def dp_fw(single, substr, target):
    N = len(target)
    ti = 0
    dp = [0] * (N+1)
    min_copy = math.ceil(substr/single)
    print(single, substr, target)
    while ti < N:
        print(ti, ":", target[ti])
        print(dp)
        dpi = ti + 1
        ss_len = min_copy
        found = 0
        found_at = -1
        st = target[ti - (ss_len - 1):ti+1]
        found = target.find(st, 0, ti)
        while found > -1 and ss_len < ti:
            found_at =  found
            ss_len += 1
            st = target[ti - (ss_len - 1):ti+1]
            found = target.find(st, 0, ti)
        if found_at >= 0:
            append_cost = dp[dpi-1]+single
            copy_cost = dp[dpi-(ss_len -1)] + substr
            dp[dpi] = min(append_cost, copy_cost)
        else:
            dp[dpi] = dp[dpi-1]+single
        ti += 1
    return dp

def cost_to_build(single, substr, target):
    table1 = dp_fw(single, substr, target)
    return table1[-1]
