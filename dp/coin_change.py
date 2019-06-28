
"""
https://www.hackerrank.com/challenges/coin-change/problem
"""


"""
took me a bit, but I understand.

first we build the table of way to make change with the smallest coin only
Then the next coin is processed, which can build on the previous, but might not

by layering in each coin denomination, we are only counting ways to build them
compared to my initial strategy which was calculating numbers of sequences.
"""
def build_dp(n, cs):
    table = [0] * (n +1)
    table[0] = 1
    for c in cs:
        for ii in range(c, n+1):
            table[ii] += table[ii-c]
    return table[n]

