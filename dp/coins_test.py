import coins

def test_recursive():
    case = 12
    expect = 13
    assert expect == coins.recursive(case)
    assert 2 == coins.recursive(2)

def test_smarter_recursive():
    case = 12
    expect = 13
    assert expect == coins.smarter_recursive(case)
    assert 2 == coins.recursive(2)

def test_iterative_loop_body_base():
    stack = []
    table = {0:0}
    stack.append(0)
    assert len(table) == 1
    coins._iterative_loop_body(stack, table)
    assert len(stack) == 0
    assert len(table) == 1

def test_iterative_loop_body_base1():
    stack = []
    table = {0:0}
    stack.append(1)
    assert len(table) == 1
    coins._iterative_loop_body(stack, table)
    assert len(stack) == 0
    assert len(table) == 2

def test_iterative_loop_body_2():
    stack = []
    table = {0:0}
    stack.append(2)
    assert len(table) == 1
    coins._iterative_loop_body(stack, table)
    assert len(stack) == 4
    assert len(table) == 1

def test_iterative_table_builder():
    table = coins._iterative_table_builder(2)
    assert len(table) == 3
    assert table[2] == 2
    assert table[1] == 1
    assert table[0] == 0

def test_iterative_table_builder_bigger():
    table = coins._iterative_table_builder(12)
    assert len(table) == 7

def test_iterative_table_builder_100():
    table = coins._iterative_table_builder(100)
    assert len(table) == 15

def test_iterative():
    case = 12
    expect = 13
    assert 2 == coins.iterative(2)
    assert expect == coins.iterative(case)
