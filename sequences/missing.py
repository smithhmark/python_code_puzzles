
def find_missing(nums):
    num = 0
    for ii, vv in enumerate(nums):
        num -= vv
        num += ii + 1

    return num
