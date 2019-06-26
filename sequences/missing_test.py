
import missing


def test():
    vals = list(range(10)) + list(range(11, 20))

    val = missing.find_missing(vals)
    assert val == 10
