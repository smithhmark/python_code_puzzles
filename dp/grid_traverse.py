
def build_table(n, m):
    #table = [[0]* m] * n
    table = []
    table.append([1] * m)
    for row in range(n-1):
        tmp = []
        tmp.append(1)
        for col in range(m-1):
            tmp.append(0)
        #table.append([[1] + [0] * (m-1)])
        table.append(tmp)

    #print(stringify_table(table))
    for row in range(1,n):
        #print("row:", row)
        #print("before:",table[row])
        for col in range(1,m):
            up_options = table[row-1][col] 
            left_options = table[row][col-1]
            table[row][col] = up_options + left_options

            #print(row,",", col, ":",table[row][col])
            #print("\t",row-1,",", col, ":up:",table[row-1][col])
            #print("\t",row,",", col-1, ":left:",table[row][col-1])
        #print("after:",table[row])
    return table

def stringify_table(table):
    tmp = []
    for row in table:
        tmp.append(",".join(str(val) for val in row))
    return "\n".join(tmp)
