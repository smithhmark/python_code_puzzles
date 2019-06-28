
import credit_card_num

valids = [
        "4253625879615786",
        "4424424424442444",
        "5122-2368-7954-3214"
        ]
invalids = [
        "42536258796157867",
        "4424444424442444",
        "5122-2368-7954 - 3214",
        "44244x4424442444",
        "0525362587961578",
        ]

def test_valid_valids():
    for ccn in valids:
        print(ccn)
        assert credit_card_num.valid(ccn)

def test_valid_invalids():
    for ccn in invalids:
        print(ccn)
        assert credit_card_num.valid(ccn) == False
