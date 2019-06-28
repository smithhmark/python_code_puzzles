"""
https://www.hackerrank.com/challenges/validating-credit-card-number/problem
"""
import re


CCN_accept = r'^[456](\d{15}|\d{3}([-]\d{4}){3})$'
CCN = re.compile(CCN_accept)

CCN_reject = r'(\d)\1\1\1'
CCNr = re.compile(CCN_reject)

def valid(ccn):
    if CCN.match(ccn):
        tmp = "".join(ccn.split('-'))
        if CCNr.search(tmp) is None:
            return True
    return False
