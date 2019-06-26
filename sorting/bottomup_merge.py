from math import ceil
from collections import defaultdict

def counting_merge(src, dest, begin, mid, end, cnts):
    ii = begin # index for left subarray
    jj = mid + 1 # index for right subarray
    out = begin
    inversions = 0 # inversions detected this merge cycle
    while ii <= mid and jj <= end:
        if src[ii] <= src[jj]:
            dest[out] = src[ii]
            cnts[src[ii]] += inversions
            ii += 1
            out += 1
        else:
            dest[out] = src[jj]
            jj += 1
            out += 1
            inversions += 1 # each time a right val goes first: add one
    while ii <= mid:
        dest[out] = src[ii]
        cnts[src[ii]] += inversions
        ii += 1
        out += 1
    while jj <= end:
        dest[out] = src[jj]
        jj += 1
        out += 1

def merge(src, dest, begin, mid, end):
    ii = begin
    jj = mid + 1
    out = begin
    while ii <= mid and jj <= end:
        if src[ii] <= src[jj]:
            dest[out] = src[ii]
            ii += 1
            out += 1
        else:
            dest[out] = src[jj]
            jj += 1
            out += 1
    while ii <= mid:
        dest[out] = src[ii]
        ii += 1
        out += 1
    while jj <= end:
        dest[out] = src[jj]
        jj += 1
        out += 1

def merge_params(sorted_len, arry_sz, window):
    window_sz = 2*sorted_len
    start = window * window_sz
    mid = start + sorted_len -1
    if mid >= arry_sz:
        return start, arry_sz - 1, 0
    end = start + window_sz - 1
    if end >= arry_sz:
        end = arry_sz-1
    return start, mid, end

def counting_sort(arry):
    sz = len(arry)
    tmp1 = list(arry)
    tmp2 = [0] * sz
    inversion_counts = defaultdict(int)

    sorted_len = 1
    to = tmp1
    frm = tmp2
    while sorted_len < sz:
        tmp = frm
        frm = to
        to = tmp
        window_sz = 2*sorted_len
        windows = ceil(sz/window_sz)
        for window in range(windows):
            params =  merge_params(sorted_len, sz, window)
            #print("params({},{},{})={}".format(sorted_len, sz,window, params))
            start, mid, end = params
            counting_merge(frm, to, start, mid, end, inversion_counts)
        #print(to)
        sorted_len = window_sz
    return to, inversion_counts

def sort(arry):
    sz = len(arry)
    tmp1 = list(arry)
    tmp2 = [0] * sz

    sorted_len = 1
    to = tmp1
    frm = tmp2
    while sorted_len < sz:
        tmp = frm
        frm = to
        to = tmp
        window_sz = 2*sorted_len
        windows = ceil(sz/window_sz)
        for window in range(windows):
            params =  merge_params(sorted_len, sz, window)
            #print("params({},{},{})={}".format(sorted_len, sz,window, params))
            start, mid, end = params
            merge(frm, to, start, mid, end)
        #print(to)
        sorted_len = window_sz
    return to
