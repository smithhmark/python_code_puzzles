

FACTORS = {}
def factor(n):
    if n not in FACTORS:
        facts = []
        for trial in range(n, 1, -1):
            if n % trial == 0:
                facts.append(trial)
        FACTORS[n] = facts
    return FACTORS[n]

def get_betweens(d1,d2):
    right_factors = None
    betweens = set()
    left = set(d1)
    for num in d2:
        facts = factor(num)
        if right_factors is None:
            right_factors = set(facts)
        else:
            right_factors.intersection_update(facts)
    print(right_factors)
    for num in right_factors:
        facts = set(factor(num))
        if left.issubset(facts):
            betweens.add(num)
    print(betweens)
    return betweens
