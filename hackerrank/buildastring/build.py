
"""
https://www.hackerrank.com/challenges/build-a-string/problem


"""
import sys
import math
import bisect

"""
012345
ab12ab
"""
def _find_longest_ending_here(target, idx, min_len=1):
    found = 0
    found_at = -1
    ss_len = min_len
    ss = target[idx - (ss_len - 1):idx + 1]
    #print("  matching from?", ss)
    found = target.find(ss, 0, idx - ss_len)
    matched = ''
    while found > -1 and ss_len *2 <= idx+1:
        found_at =  found
        matched = ss
        ss_len += 1
        ss = target[idx - (ss_len - 1):idx + 1]
        found = target.find(ss, 0, idx - ss_len+1)
        #print("    matching?", ss)
        #print("    found?", found)
        #print("    ss_len", ss_len, "?<=", idx)
    if found_at > -1:
        return matched, found_at
    else:
        return '', -1

def lcp(left, right):
    cnt = 0
    for li, ri in zip(left, right):
        if li == ri:
            cnt += 1
        else:
            return cnt
    return cnt

def _find_longest_starting_here(target, idx, min_len=1):
    N=len(target)
    found = 0
    found_at = -1
    ss_len = min_len
    ss = target[idx:idx+ss_len]
    #print("  matching from?", st)
    found = target.find(ss, 0, idx)
    matched = ''
    while found > -1 and ss_len <= idx and idx + ss_len <= N:
        found_at =  found
        matched = ss
        ss_len += 1
        ss = target[idx:idx+ss_len]
        found = target.find(ss, found, idx)
            #print("    matching?", st)
            #print("    found?", found)
            #print("    ss_len", ss_len, "?<", ti)
            #print("    ti+ss_len=", ti+ss_len, " is ", ti+ss_len <= N)
    if found_at > -1:
        return matched, found_at
    else:
        return None, None

def longest_prefix(target, ti, prefs):
    ss = target[ti]
    left = bisect.bisect_left(prefs, (ss, ti))
    right = bisect.bisect_right(prefs, (chr(ord(ss) + 1),ti))
    back = 1
    while prefs[left].startswith(ss) :
        back += 1
        ss = target[ti-back:ti+1]
        ss = ss[::-1]
        left = bisect.bisect_left(prefs, target[ti], left, right)

def build_inv_prefix_array(target):
    N = len(target)
    prefs = []
    rtarg = target[::-1]
    for ii in range(N):
        prefs.append((rtarg[ii:], (N-1) -ii))
    prefs.sort()
    return prefs

def build_lcp_array(suffs):
    lcps = []
    for ii in range(1, len(suffs)):
        lcps.append(lcp(suffs[ii-1], suffs[ii]))
    return lcps

def find_longest_prestring(target, idx, iprefs):
    N = len(iprefs)
    #leftward_prefs = list(filter(lambda x: x[1] <= idx, iprefs))
    #print("t:", target, "i:", idx)
    #print("iprefs:", iprefs)
    cc = target[idx]
    leftward_prefs =iprefs
    right_limit = bisect.bisect_right(leftward_prefs, (chr(ord(cc) + 1),idx))
    #print("right_limit:", right_limit)
    #print("initial ri based on", target[:idx+1][::-1])
    ri = bisect.bisect_right(leftward_prefs, (target[:idx+1][::-1], ))
    li = ri -1
    #print("  ri:", ri)
    lcp1 =  0
    lcp2 =  0
    if ri == 0:
        #print("  nolonger returning")
        lcp1 = 0
    else:
        while li >=0 and leftward_prefs[li][1] >= leftward_prefs[ri][1]:
            li -= 1
        #print("  li:", li)
        lcp1 = lcp(leftward_prefs[li][0], leftward_prefs[ri][0])
        pos_dif = leftward_prefs[ri][1] - leftward_prefs[li][1]
        if lcp1 > pos_dif:
            # could have overlap
            lcp1 = pos_dif
            if li > 0:
                li -= 1 # try next one
                while li >=0 and leftward_prefs[li][1] >= leftward_prefs[ri][1]:
                    li -= 1
                if li > -1:
                    #print("trying at:", li)
                    hmm = lcp(leftward_prefs[li][0], leftward_prefs[ri][0])
                    #print("hmm:", hmm)
                    if hmm > pos_dif:
                        lcp1 = hmm
    li = ri
    if li == N-1:
        lcp2 = 0
    else:
        ri = li + 1
        while ri < right_limit and leftward_prefs[ri][1] >= leftward_prefs[li][1]:
            ri += 1
        #print("  ri:", ri)
        if ri == right_limit:
            lcp2 = 0
        else:
            lcp2 = lcp(leftward_prefs[li][0], leftward_prefs[ri][0])
            pos_dif = leftward_prefs[li][1] - leftward_prefs[ri][1]
            if lcp2 > pos_dif:
                #could have overlap
                lcp2 = pos_dif
                ri += 1
                while (ri < right_limit 
                        and leftward_prefs[ri][1] >= leftward_prefs[li][1]):
                    ri += 1
                if ri < right_limit:
                    hmm = lcp(leftward_prefs[li][0], leftward_prefs[ri][0])
                    if hmm > pos_dif:
                        lcp2 = hmm
    #print("  lcp1", lcp1)
    #print("  lcp2", lcp2)
    return max(lcp1, lcp2)

def dp_fw(single, substr, target):
    N = len(target)
    ti = 0
    dp = [0] * (N+1)
    iprefs = build_inv_prefix_array(target)
    #print(single, substr, target)
    while ti < N:
        #print(" {} : {}".format(ti,target[ti]))
        dpi = ti + 1
        append_cost = dp[dpi-1] + single
        #print(" finding longest")
        #matched, whr = _find_longest_ending_here(target, ti)
        #matched_len = len(matched)
        matched_len = find_longest_prestring(target, ti, iprefs)
        #print("@", ti, "longest:'{}'".format(target[ti-(matched_len-1):ti+1]))
        if matched_len == 0:
            #copy_cost = sys.maxsize
            dp[dpi] = append_cost
        else:
            copy_cost = substr + dp[dpi-matched_len]
            final_cost = min(append_cost, copy_cost)
            dp[dpi] = final_cost
        ti += 1
    return dp

def scan_for_prefix(target):
    N = len(target)
    jumps = [-1] * (N)
    prevs = [-1] * (N)
    prefs = {}
    ii = N - 1
    longest, whr = _find_longest_ending_here(target, ii)
    #print(" found:", longest)
    while ii > 0:
        if longest:
            matched_len = len(longest)
            prev_idx = ii - matched_len
            for jj in range(ii - matched_len+1, ii+1):
                jumps[jj] = whr
                prevs[jj] = prev_idx
                prefs[jj] = longest[:jj - (ii - matched_len +1) + 1]
            ii -= matched_len
        else:
            ii -= 1
        #print("   ii:", ii, "target:", target[:ii+1])
        longest, whr = _find_longest_ending_here(target, ii, 1)
        #print("   found:", longest)
    return jumps, prefs, prevs

def cost_to_build(single, substr, target):
    table1 = dp_fw(single, substr, target)
    return table1[-1]
    #return recursive(single, substr, target)

SUBSTR_MEMO = {}
COST_MEMO = {}
def _recur_append(single, substr, target, idx, cost):
    #print(" " * idx, "A:",target[idx], idx, cost)
    cost_id =(target, idx, single, substr, "A")
    if cost_id in COST_MEMO:
        prior_cost = COST_MEMO.get(cost_id)
        return prior_cost
    tmp = cost + single
    if idx == len(target) - 1:
        return tmp
    next_idx = idx + 1
    #print("next idx:", next_idx)
    final = min(
            _recur_copy(single, substr, target, next_idx, tmp),
            _recur_append(single, substr, target, next_idx, tmp))
    
    COST_MEMO[cost_id] = final
    return final

def _recur_copy(single, substr, target, idx, cost):
    min_width = _min_width(single, substr)
    longest_here = SUBSTR_MEMO.get((target, idx, min_width))
    if not longest_here:
        tmp = cost + single
        #print("ahhhh")
        return sys.maxsize
        return _recur_append(single, substr, target, idx, tmp)
        #longest_here, found_at = _find_longest_starting_here(target, idx)
        #SUBSTR_MEMO[(target, idx)] = longest_here
    else:
        #print(" " * idx, "A:",target[idx], idx, cost)
        tmp = cost + substr
        llen = len(longest_here)
        next_idx = idx + llen -1
        if next_idx == len(target) -1:
            return tmp
        elif next_idx > len(target) -1:
            #print("ahhhh", longest_here)
            return tmp
        else:
            #print("nxt idx:", next_idx)
            return min(
                    _recur_copy(single, substr, target, next_idx, tmp),
                    _recur_append(single, substr, target, next_idx, tmp))
        
def _min_width(single, substr):
    return math.ceil(substr/single)

def recursive_forward(single, substr, target):
    min_width = _min_width(single, substr)
    any_usable_substr = False
    for ii in range(len(target)):
        longest, whr = _find_longest_starting_here(target, ii, min_width)
        SUBSTR_MEMO[(target, ii, min_width)] = longest
        if longest is not None:
            any_usable_substr = True
    if any_usable_substr:
        return min(
            _recur_copy(single, substr, target, 0, 0),
            _recur_append(single, substr, target, 0, 0))
    else:
        return len(target) * single

COST_MEMO = {}
def _recur(single, substr, target, idx):
    cost_id =(target, idx, single, substr)
    prior_cost = COST_MEMO.get(cost_id)
    #prior_cost = None
    if prior_cost:
        return prior_cost
    if idx == 0 :
        COST_MEMO[cost_id] = single
        #print(" " * idx,idx, target[idx], "acost:",single)
        return single
    append_cost = single + _recur(single, substr, target, idx -1)
    #print(" " * idx,idx, target[idx], "acost:",append_cost)
    min_width = _min_width(single, substr)
    longest, whr = _find_longest_ending_here(target, idx, min_width)
    if longest:
        matched_len = len(longest)
        copy_cost = substr + _recur(single, substr, target, idx-matched_len)
        #print(" " * idx,idx, target[idx], "ccost:",copy_cost, "l:",longest)
    else:
        copy_cost = sys.maxsize
    final_cost = min(append_cost, copy_cost)
    COST_MEMO[cost_id] = final_cost
    return final_cost

def recursive_back(single, substr, target):
    N = len(target)
    return _recur(single, substr, target, N-1)

def recursive(single, substr, target):
    return recursive_back(single, substr, target)
