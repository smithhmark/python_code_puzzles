
"""
https://www.hackerrank.com/challenges/build-a-string/problem


"""
import sys
import math

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
        return None, None

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

def dp_fw(single, substr, target):
    N = len(target)
    ti = 0
    dp = [0] * (N+1)
    min_copy = math.ceil(substr/single)
    #print(single, substr, target)
    while ti < N:
        print(" {} : {}".format(ti,target[ti]))
        dpi = ti + 1
        ss_len = min_copy
        found = 0
        found_at = -1
        st = target[ti:ti+ss_len]
        #print("  matching from?", st)
        found = target.find(st, 0, ti)
        matched = ''
        while found > -1 and ss_len <= ti and ti + ss_len <= N:
            found_at =  found
            matched = st
            ss_len += 1
            st = target[ti:ti+ss_len]
            found = target.find(st, found, ti)
            #print("    matching?", st)
            #print("    found?", found)
            #print("    ss_len", ss_len, "?<", ti)
            #print("    ti+ss_len=", ti+ss_len, " is ", ti+ss_len <= N)
        if found_at >= 0:
            #print("   found '{}' at {}".format(st, found_at))
            #print("   matched '{}' at {}".format(matched, found_at))
            ss_len -= 1
            matched_len = len(matched)
            append_cost = dp[dpi-1]+(matched_len * single)
            #print("    acost", append_cost)
            copy_cost = dp[dpi-1]+substr
            #print("    ccost", copy_cost)
            if append_cost < copy_cost:
                dp[dpi] = dp[dpi-1]+single
                ti += 1
            else:
                for offset in range(matched_len):
                    dp[dpi + offset] = copy_cost
                #print("  jumping fwd:",matched_len)
                dp[dpi+matched_len-1] = copy_cost
                ti += len(matched)
        else:
            dp[dpi] = dp[dpi-1]+single
            ti += 1
        #print(dp)
        #print([], list(target))
    return dp

def cost_to_build(single, substr, target):
    #table1 = dp_fw(single, substr, target)
    #return table1[-1]
    return recursive(single, substr, target)

SUBSTR_MEMO = {}
COST_MEMO = {}
def _recur_append(single, substr, target, idx, cost):
    print(" " * idx, "A:",target[idx], idx, cost)
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
        print(" " * idx, "A:",target[idx], idx, cost)
        tmp = cost + substr
        llen = len(longest_here)
        next_idx = idx + llen -1
        if next_idx == len(target) -1:
            return tmp
        elif next_idx > len(target) -1:
            print("ahhhh", longest_here)
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
        print(" " * idx,idx, target[idx], "acost:",single)
        return single
    append_cost = single + _recur(single, substr, target, idx -1)
    print(" " * idx,idx, target[idx], "acost:",append_cost)
    min_width = _min_width(single, substr)
    longest, whr = _find_longest_ending_here(target, idx, min_width)
    if longest is not None:
        matched_len = len(longest)
        copy_cost = substr + _recur(single, substr, target, idx-matched_len)
        print(" " * idx,idx, target[idx], "ccost:",copy_cost, "l:",longest)
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
