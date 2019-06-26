import acode

def test_encode_letter():
    assert acode.encode_letter("a") == "1"
    assert acode.encode_letter("n") == "14"

def test_build_decode_count_table_24():
    table = acode.build_decode_count_table("24")
    assert table[0] == 1
    assert table[1] == 2

def test_build_decode_count_table_33():
    table = acode.build_decode_count_table("33")
    assert table[0] == 1
    assert table[1] == 1

def test_build_decode_count_table_1():
    table = acode.build_decode_count_table("1")
    assert table[0] == 1

def test_build_decode_count_table_11():
    table = acode.build_decode_count_table("11")
    assert table[0] == 1
    assert table[1] == 2

def test_build_decode_count_table_111():
    table = acode.build_decode_count_table("111")
    assert table[0] == 1
    assert table[1] == 2
    assert table[2] == 3

def test_encode_string():
    assert acode.encode_string("BEAN") == "25114"

def test_count_decodes_bob():
    assert acode.count_decodes("25114") == 6

def test_count_decodes_case2():
    assert acode.count_decodes("1111111111") == 89

def test_count_decodes_case3():
    assert acode.count_decodes("3333333333") == 1

def test_count_decodes_case_bad_input():
    assert acode.count_decodes("0") == 0

