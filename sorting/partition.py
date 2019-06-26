

def partition(arry, pivot):
    first_big = 0
    for ii, val in enumerate(arry):
        if (val < pivot):
            tmp = val
            arry[ii] = arry[first_big] 
            arry[first_big] = tmp
            first_big += 1
    return first_big
