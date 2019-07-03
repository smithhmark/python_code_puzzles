
"""
https://www.hackerrank.com/challenges/build-a-string/problem


"""


def cost_to_build(single, substr, target):
    """
    single - the cost to add an arbetrary char to the end
    substr = the cost to add a copy of an already build substring to end
    target - the string we wish to build
    """

    alphabet = set()
    ii = 0
    N = len(target)
    table = [0] * N
    while ii < N:
        cc = target[ii]
        if cc not in alphabet:
            print("first time seeing:", cc)
            if ii == 0:
                table[ii] = single
            else:
                table[ii] = single + table[ii-1]
            alphabet.add(cc)
            ii += 1
        else:
            # want the longest substring target[ii:n] that is contained in tartet[:ii]
            addable=""
            found = 0
            for reach in range(1,ii+1):
                #print("reaching forward", target[ii:ii+reach])
                found = target.find(target[ii:ii+reach], found, ii)
                if found > -1:
                    #print("  found substr at", found)
                    addable = target[ii:ii+reach]
                else:
                    break
            print("longest substr", addable)
            single_cost = len(addable) * single
            if single_cost < substr:
                print("  char-by-char cheaper than block copy")
                table[ii] = table[ii-1] + single
                ii += 1
                #for jj in range(len(addable)):
                #    table[ii+jj] = table[ii+jj -1] + single
            else:
                print("  block copy cheaper than char-by-char")
                for jj in range(len(addable)):
                    table[ii+jj] = table[ii-1] + substr
                ii += len(addable)
    #print(list(target))
    print(target)
    #print(table)
    print("\n".join("{:3}: {},{:3}".format(*ii) for ii in  zip(range(N), target, table)))
    return table[-1]
