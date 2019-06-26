
import bottomup_merge as merge

def brute(vals):
    output = []
    for ii, val in enumerate(vals):
        cnt = 0
        for jj in range(ii, len(vals)):
            if vals[jj] > val:
                cnt += 1
        output.append(cnt)
    return output

def get_counts(vals):
    temp = list(vals)
    srtd, inversions = merge.counting_sort(temp)

    output = []
    last_idx = len(vals) - 1
    for ii, val in enumerate(vals):
        output.append(last_idx - ii - inversions[val])

    return output
