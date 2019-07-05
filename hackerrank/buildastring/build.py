
"""
https://www.hackerrank.com/challenges/build-a-string/problem


"""
import math

def cost_to_build_backward(single, substr, target):
    """
    single - the cost to add an arbetrary char to the end
    substr = the cost to add a copy of an already build substring to end
    target - the string we wish to build
    """
    table = backward_table(single, substr, target)
    return table[0]

def dp_fw(single, substr, target):
    N = len(target)
    ti = 0
    dp = [0] * (N+1)
    min_copy = math.ceil(substr/single)
    print(single, substr, target)
    while ti < N:
        print(ti, ":", target[ti])
        print(dp)
        dpi = ti + 1
        ss_len = min_copy
        found = 0
        found_at = -1
        st = target[ti - (ss_len - 1):ti+1]
        found = target.find(st, 0, ti)
        while found > -1 and ss_len < ti:
            found_at =  found
            ss_len += 1
            st = target[ti - (ss_len - 1):ti+1]
            found = target.find(st, 0, ti)
        if found_at >= 0:
            append_cost = dp[dpi-1]+single
            copy_cost = dp[dpi-(ss_len -1)] + substr
            dp[dpi] = min(append_cost, copy_cost)
        else:
            dp[dpi] = dp[dpi-1]+single
        ti += 1
    return dp

def backward_table(single, substr, target):
    print("backward")
    N = len(target)
    ii = N-1
    table = [0] * (N+1)
    min_copy = math.ceil(substr/single)
    #print("min_copy:", min_copy)
    while ii > -1:
        print("  working index:", ii, target[ii])
        #print("table:", table)
        #how much can we copy...
        if ii >= 2*min_copy - 1:
            #print("working copiable index:", ii)
            found = 0
            ss_len = min_copy
            if ii - (ss_len -1) < 0:
                found = target.find(target[0:ii+1],0,ii-ss_len+1)
            else:
                found = target.find(target[ii-(ss_len-1):ii+1],0,ii-ss_len+1)
            #print("  looking for", target[ii-(ss_len-1):ii+1])
            fnd_at = -1
            while found >= 0:
                ##print("    found", target[ii-(ss_len-1):ii+1])
                fnd_at = found
                ss_len += 1
                #print("    now looking for", target[ii-(ss_len-1):ii+1])
                found = target.find(target[ii-(ss_len-1):ii+1],0,ii-(ss_len-1))
            if fnd_at < 0: #ss_len == min_copy:
                print("    no useful substring")
                # going to need to add one-by-one
                table[ii] = table[ii+1] + single
                ii -= 1
            else:
                ss_len -= 1 # substring length is too high cuz we exit loop
                print("    found copiable substr:'{}' at {}".format(
                    target[ii-(ss_len-1):ii+1], fnd_at))
                """
                print("  len ={}".format(len(target[ii-(ss_len-1):ii+1])))
                """
                table[ii] = table[ii+1] + substr
                table[ii-(ss_len) + 1] = table[ii]
                ii -= ss_len
        else:
            # no way to copy
            #print("working non-copiable index:", ii)
            table[ii] = table[ii+1] + single
            ii -= 1
            
    #print(list(target))
    #print(target)
    #print(table)
    #print("\n".join("{:3}: {},{:3}".format(*ii) for ii in  zip(range(N), target, table)))
    return table

def stringify_table(table, target):
    N = len(target)
    return "\n".join("{:3}: {},{:3}".format(*ii) for ii in  zip(range(N), target, table))

def cost_to_build(single, substr, target):
    #return cost_to_build_backward(single, substr, target)
    table1 = forward_table(single, substr, target)
    table2 = backward_table(single, substr, target)
    return min(table1[-1],table2[0])
    #return cost_to_build_forward(single, substr, target)

def cost_backward(single, substr, target):
    """
    single - the cost to add an arbetrary char to the end
    substr = the cost to add a copy of an already build substring to end
    target - the string we wish to build
    """
    return cost_to_build_backward(single, substr, target)

def cost_forward(single, substr, target):
    """
    single - the cost to add an arbetrary char to the end
    substr = the cost to add a copy of an already build substring to end
    target - the string we wish to build
    """
    return cost_to_build_forward(single, substr, target)

def cost_to_build_forward(single, substr, target):
    """
    single - the cost to add an arbetrary char to the end
    substr = the cost to add a copy of an already build substring to end
    target - the string we wish to build
    """
    table = forward_table(single, substr, target)
    return table[-1]

def forward_table(single, substr, target):
    print("forward")
    alphabet = set()
    N = len(target)
    table = [0] * (N)
    table[0] = single
    ii = 0
    #alphabet.add(target[0])
    min_copy = math.ceil(substr/single)
    print("min copy width=", min_copy)
    print("min copy width={}/{}".format(substr, single))
    while ii < N:
        cc = target[ii]
        print("  working index", ii, cc)
        if cc not in alphabet:
            print("    first time seeing:", cc)
            if ii == 0:
                table[ii] = single
            else:
                table[ii] = single + table[ii-1]
            alphabet.add(cc)
            ii += 1
        else:
            # want the longest substring target[ii:n] that is contained in tartet[:ii]
            found = 0
            ss_len = min_copy
            #print("reaching from {} at {}".format(cc, ii))
            print("    looking for", target[ii:ii+ss_len])
            found = target.find(target[ii:ii+ss_len], found, ii)
            #print("      found", found)
            fnd_at = -1
            while found >= 0 and ss_len <= ii and ii+ss_len <= N:
                fnd_at = found
                """
                print("      found '{}' at {}".format(
                    target[ii:ii+ss_len], fnd_at))
                """
                ss_len += 1
                #print("      ss_len:", ss_len)
                #print("      looking for", target[ii:ii+ss_len])
                found = target.find(target[ii:ii+ss_len], found, ii)
            if fnd_at < 0:
                print("    char-by-char cheaper than block copy")
                table[ii] = table[ii-1] + single
                ii += 1
            else:
                ss_len -= 1
                print("    found copiable substr:'{}' at {}".format(
                    target[ii: ii +ss_len], fnd_at))
                #print("  block copy cheaper than char-by-char")
                #print("  table[", ii+(ss_len-1), "] = ",table[ii-1] + substr)
                table[ii] = table[ii-1] + substr
                table[ii+(ss_len-1)] = table[ii-1] + substr
                ii += ss_len
    #print(list(target))
    #print(target)
    #print(table)
    #print("\n".join("{:3}: {},{:3}".format(*ii) for ii in  zip(range(len(table)), target, table)))
    return table

def interpret_ft(table, a, b):
    norm = []
    prev = None
    for cur in table:
        if cur == prev or cur == 0:
            norm.append('b')
        else:
            if prev is None:
                norm.append('a')
            else:
                diff = cur - prev
                if diff == a:
                    norm.append('a')
                elif diff == b:
                    norm.append('b')
                else:
                    norm.append('*')
            prev = cur
    return norm

def interpret_bt(table, a, b):
    norm = []
    prev = None
    for cur in reversed(table[:-1]):
        if cur == prev or cur == 0:
            norm.append('b')
        else:
            if prev is None:
                prev = 0
            diff = cur - prev
            if diff == a:
                norm.append('a')
            elif diff == b:
                norm.append('b')
            else:
                norm.append('*')
            prev = cur
    norm.reverse()
    return norm

def compare_tbls(ft, bt):
    t1 = interpret_ft(ft)
    t2 = interpret_bt(bt)
    return compare_tis(t1,t2)
def compare_tis(t1,t2):
    diff = []
    for l, r in zip(t1, t2):
        if l == r:
            diff.append(' ')
        else:
            diff.append('*')
    return diff
