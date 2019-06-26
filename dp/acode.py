
"""
see (https://www.spoj.com/problems/ACODE/) 
"""

def encode_letter(letter):
    return str(ord(letter.lower()[0]) - ord("a"[0])  +1)

def encode_string(ss):
    return "".join(encode_letter(cc) for cc in ss)


valid_one_char = set("123456789")

valid_first_of_two = set("12")
valid_after_one = set("1234567890")
valid_after_two = set("0123456")

def build_decode_count_table(ct):
    table = [0] * len(ct)

    for ii, cc in enumerate(ct):
        if ii == 0:
            if cc in valid_one_char:
                table[ii] = 1
            else:
                return table
        elif ii == 1:
            twodigitcount = 0
            onedigitcount = 0
            if cc in valid_one_char:
                onedigitcount = 1
            if ct[ii-1] == "1" and cc in valid_after_one:
                twodigitcount = 1
            if ct[ii-1] == "2" and cc in valid_after_two:
                twodigitcount = 1
            table[ii] = onedigitcount + twodigitcount
        else:
            onedigitcount = 0
            twodigitcount = 0
            if cc in valid_one_char:
                onedigitcount = 1

            if ct[ii-1] == "1" and cc in valid_after_one:
                twodigitcount = 1
            if ct[ii-1] == "2" and cc in valid_after_two:
                twodigitcount = 1

            table[ii] = table[ii-1] * onedigitcount + table[ii-2] * twodigitcount
    return table


def count_decodes(ct):
    table = build_decode_count_table(ct)
    return table[-1]
