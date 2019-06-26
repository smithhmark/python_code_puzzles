"""
see (https://www.spoj.com/problems/COINS/) for problem description
"""

def recursive(n):
    if n < 1:
        return 0
    half = recursive(n//2)
    third = recursive(n//3)
    quarter = recursive(n//4)
    split = half + third + quarter
    if n > split:
        return n
    else:
        return split

STATES = {}
def smarter_recursive(n):
    if n in STATES:
        return STATES[n]

    if n < 1:
        return 0
    half = smarter_recursive(n//2)
    third = smarter_recursive(n//3)
    quarter = smarter_recursive(n//4)
    split = half + third + quarter
    if n > split:
        STATES[n] = n
        return n
    else:
        STATES[n] = split
        return split

def _iterative_loop_body(problem_stack, soln_table):
    cur_problem = problem_stack.pop()
    half = cur_problem//2
    third = cur_problem//3
    quarter = cur_problem//4
    half_soln = soln_table.get(half)
    third_soln = soln_table.get(third)
    quarter_soln = soln_table.get(quarter)
    if (half_soln is not None 
        and third_soln is not None 
        and quarter_soln is not None):
            soln_summ = half_soln + third_soln + quarter_soln
            if cur_problem > soln_summ:
                soln_table[cur_problem] = cur_problem
            else:
                soln_table[cur_problem] = soln_summ
    else:
        # a bit wasteful
        problem_stack.append(cur_problem)
        problem_stack.append(half)
        problem_stack.append(third)
        problem_stack.append(quarter)

def _iterative_table_builder(n):
    table = {
            0: 0,
            1: 1,
            }
    problem_stack = []
    problem_stack.append(n)
    while len(problem_stack) > 0:
        _iterative_loop_body(problem_stack, table)
    return table

def iterative(n):
    table = _iterative_table_builder(n)
    return table[n]
