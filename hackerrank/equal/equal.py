"""
https://www.hackerrank.com/challenges/equal/problem


given:
  * an array mapping locations to inventories
  * a list of possible additions

query:
    how many rounds of additions does it take to make it so all inventories are
equal.
each round, all locations but on get the same addition.

note:
    comments in https://github.com/BlakeBrown/HackerRank-Solutions/blob/master/Algorithms/Dynamic%20Programming/Equal%20-%20O(n)%20greedy.cpp
    were very helpful
"""
import sys

def rounds_between(n1, n2, rs=[1,2,5]):
    diff = abs(n1-n2)
    rounds = 0
    if diff > 0:
        for rr in reversed(rs):
            d, m = divmod(diff, rr)
            rounds += d
            diff = m
        if rounds == 0:
            return -1
        else:
            return rounds
    else:
        return 0

def find_first_gap(ns, start_at=0):
    for ii in range(start_at, len(ns)-1):
        if ns[ii+1] > ns[ii]:
            return ii+1
    return -1

def find_min_actions(cookies):
    """
    this solution adapted from:https://hackerranksolutionc.blogspot.com/2017/09/equal-hackerrank-solution.html
    """
    cookies.sort()
    sm = sys.maxsize

    for base in range(3):
        cur_sum = 0
        for ii in range(len(cookies)):
            delta = cookies[ii] - cookies[0] + base
            cur_sum += rounds_between(0, delta)
        sm = min(sm, cur_sum)
    return sm

def _build_table_down(ns, rs):
    mnvl = min(ns)
    c_0 = 0
    c_mn = 0
    costs = [0] * 5
    for ii in range(len(ns)):
        for fudge, cost in enumerate(costs):
            if cost is not None:
                rnds = rounds_between(mnvl, fudge+ns[ii], rs)
                if rnds == -1:
                    costs[fudge] = None
                else:
                    costs[fudge] = cost + rnds
    return costs

def build_table_down(ns, rs):
    costs = _build_table_down(ns, rs)
    #print("costs:",costs)
    return min(filter(lambda x: x is not None, costs))

def build_differences(ns):
    diffs = []
    for ii in range(len(ns)-1):
        diffs.append(ns[ii+1] - ns[ii])
    return diffs

def min_rounds(ns, rs=[1,2,5]):
    dp = build_table_down(ns, rs)
    return dp
