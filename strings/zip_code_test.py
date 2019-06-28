#import re

import zip_code

valid = [
        "111456"
        ]
invalid = [
        "110000"
        ]

def test_valid():
    for zp in valid:
        assert zip_code.valid(zp)
    for zp in invalid:
        assert zip_code.valid(zp) == False
