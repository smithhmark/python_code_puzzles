import partition


def test_part1():
    data = [-1,-2,-3]
    j = partition.partition(data, 0)
    assert j == 3
    data = [1,2,3]
    j = partition.partition(data, 0)
    assert j == 0

def test_part2():
    data = list(range(-5, 5))
    j = partition.partition(data, 0)
    print(data)
    assert j == 5

    data = list(range(5, -5, -1))
    j = partition.partition(data, 0)
    print(data)
    assert j == 4
