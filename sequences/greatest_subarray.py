

def brute(vals, return_location=False):
    best = None
    left, right = 0,0 
    best = vals[0]
    for ii in range(len(vals)):
        tot = vals[ii]
        if tot > best:
            best = tot
            left, right = ii, ii
        for jj in range(ii + 1, len(vals)):
            tot += vals[jj]
            if tot > best:
                best = tot
                left, right = ii, jj
    if not return_location:
        return best
    else:
        return best, (left, right)

def build_kadane_table(vals):
    table = [0]*len(vals)
    table[0] = vals[0]
    for ii in range(1, len(vals)):
        if table[ii-1] < 0:
            table[ii] = vals[ii]
        else:
            table[ii] = table[ii-1] + vals[ii]
    return table

def kadane(vals):
    table = build_kadane_table(vals)
    return max(table)

def find_endpoints(vals):
    table = build_kadane_table(vals)
    tot = max(table)
    right = table.index(tot)
    left = right
    #while left >= 0 and tot > 0:
    if tot > 0:
        while tot > 0:
            tot -= vals[left]
            left -= 1
        return left + 1, right
    else:
        return left, right
        
