import min_acceptable_substrings
import re
import math

def char_run(string):
    if re.match(r"^\d+$", string) or re.match(r"^[a-z]+$", string):
        return True
    return False

def perf_square_hex(string):
    try:
        val = int(string, 16)
        #print(val)
        val = math.sqrt(val)
        if val.is_integer(): #isinstance(val, float):
            #print(val)
            return True
        else:
            return False
    except ValueError:
        return False
    return False

def test_leftmost():
    s = "123ab"
    assert min_acceptable_substrings.leftmost(s, 0, len(s), char_run) == 2
    s = "ab"
    assert min_acceptable_substrings.leftmost(s, 0, len(s), char_run) == 1
    s = "123ab"
    assert min_acceptable_substrings.leftmost(s, 3, len(s), char_run) == 4

def test_min_brute_tricky():
    s = "123ab12"
    assert min_acceptable_substrings.brute(s, char_run) == 3

def test_min_dp_tricky():
    s = "123ab12"
    assert min_acceptable_substrings.dp(s, char_run) == 3

def test_min_brute():
    s = "123ab"
    assert min_acceptable_substrings.brute(s, char_run) == 2
    s = "123"
    assert min_acceptable_substrings.brute(s, char_run) == 1

def test_min_brute_rejects():
    s = "****"
    assert min_acceptable_substrings.brute(s, char_run) == -1
    s = "1111****"
    assert min_acceptable_substrings.brute(s, char_run) == -1
    s = "1111*11111"
    assert min_acceptable_substrings.brute(s, char_run) == -1

def test_db_accepts():
    s = "123ab"
    assert min_acceptable_substrings.dp(s, char_run) == 2
    s = "123"
    assert min_acceptable_substrings.dp(s, char_run) == 1

def test_dp_rejects():
    s = "****"
    assert min_acceptable_substrings.dp(s, char_run) == -1
    s = "1111****"
    assert min_acceptable_substrings.dp(s, char_run) == -1
    s = "1111*11111"
    assert min_acceptable_substrings.dp(s, char_run) == -1

def test_PSH():
    test_str = hex(3001 * 3001)#[2:]
    print(test_str)
    assert perf_square_hex(test_str) == True

def test_count_PHS():
    test_str = hex(3001 * 3001)[2:]
    assert min_acceptable_substrings.brute(test_str, perf_square_hex) == 1

    test_str= '44'
    assert min_acceptable_substrings.brute(test_str, perf_square_hex) == 2
