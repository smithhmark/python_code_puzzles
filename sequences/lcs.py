

def binary_width(num):
    string_rep = bin(num)[2:]
    return len(string_rep)

def binary_1s(num, normalize_to=False):
    ret = []
    string_rep = bin(num)[2:]
    actual_wdith = len(string_rep)
    for ii, digit in enumerate(string_rep):
        if digit == "1":
            ret.append(ii)
    if normalize_to is not None and actual_wdith < normalize_to:
        pad = normalize_to - actual_wdith - 1
        ret = [ vv + pad for vv in ret]
    return ret

def powerset_str(seq):
    ps = powerset(seq)
    return ["".join(ss) for ss in ps]

def powerset(seq):
    #print("seq:", seq)
    sz = len(seq)
    #print("seq len:", sz)
    ps = []
    ps_sz = 2 ** sz
    #print("ps_sz:", ps_sz)
    binwidth = binary_width(ps_sz)
    for ii in range(ps_sz):
        tmp = []
        to_include = binary_1s(ii, binwidth)
        #print("to_include:", to_include)
        for jj in to_include:
            tmp.append(seq[jj])
        ps.append(tmp)
        #ps.append("".join(tmp))
    return ps

def brute(seq1, seq2):
    ps1 = set(powerset_str(seq1))
    ps2 = set(powerset_str(seq2))
    #print(len(ps1))
    #print(ps1)
    #print(len(ps2))
    #print(ps2)
    longest = None
    sz = 0
    ps = ps1 & ps2
    #print(len(ps))
    for seq in ps:
        if len(seq) > sz:
            sz = len(seq)
            longest = seq
    return sz, longest

def stringify_table(tab):
    return "\n".join([",".join(str(ii) for ii in row) for row in tab])

def build_dp_table(seq1, seq2):
    n = len(seq1)
    m = len(seq2)
    table = [ [0 for jj in range(m+1)] for ii in range(n+1)]

    for ii in range(1, n+1):
        for jj in range(1, m+1):
            if seq1[ii-1] == seq2[jj-1]:
                table[ii][jj] = table[ii-1][jj-1] + 1
            else:
                table[ii][jj] = max(table[ii-1][jj], table[ii][jj-1])
    return table

def length_dp(seq1, seq2):
    table = build_dp_table(seq1, seq2)
    return table[-1][-1]

def read_db_table(table):
    row = len(table) -1
    col = len(table[0]) -1
    col_idxs= []
    row_idxs= []
    while row > 0 and col > 0:
        print("r:",row, "c:", col)
        if table[row][col-1] < table[row-1][col]:
            row -= 1
        elif table[row][col-1] > table[row-1][col]:
            col -= 1
        else:
            if table[row][col] > table[row-1][col]:
                # make note of this
                row_idxs.append(row)
                col_idxs.append(col)
                row -= 1
            else:
                row -= 1
    row_idxs.reverse()
    col_idxs.reverse()
    return row_idxs, col_idxs

def lcs_dp(seq1, seq2):
    table = build_dp_table(seq1, seq2)
    ri, ci = read_db_table(table)
    print(ri)
    print(ci)
    row_sub = []
    for ii in ri:
        row_sub.append(seq1[ii-1])
    col_sub = []
    for ii in ci:
        col_sub.append(seq2[ii-1])
    return row_sub, col_sub
