from math import ceil

def ring_bounds(matrix, ring):
    top_row_idx = 0 + ring
    bottom_row_idx = len(matrix) - 1 - ring
    if top_row_idx >= bottom_row_idx:
        print("oops")
        print(top_row_idx, bottom_row_idx)
        return None, None, None, None
    left_col_idx = 0 + ring
    right_col_idx = len(matrix[0]) - 1 - ring
    if left_col_idx >= right_col_idx:
        print("oops")
        print(top_row_idx, bottom_row_idx)
        return None, None, None, None
    return top_row_idx, bottom_row_idx, left_col_idx, right_col_idx

def rotate_ring_counterclockwise(matrix, ring):
    tmp = None
    top_row_idx, bottom_row_idx, left_col_idx, right_col_idx = ring_bounds(
            matrix, ring)

    if top_row_idx is None:
        return
    # down left side
    print(matrix, tmp)
    for row in range(top_row_idx, bottom_row_idx+1):
        tmp2 = matrix[row][left_col_idx]
        matrix[row][left_col_idx] = tmp
        tmp = tmp2
    print(matrix, tmp)
    # across bottom
    for col in range(left_col_idx+1, right_col_idx+1):
        tmp2 = matrix[bottom_row_idx][col]
        matrix[bottom_row_idx][col] = tmp
        tmp = tmp2
    print(matrix, tmp)
    # up right side
    for row in range(bottom_row_idx - 1, top_row_idx -1, -1):
        tmp2 = matrix[row][right_col_idx]
        matrix[row][right_col_idx] = tmp
        tmp = tmp2
    print(matrix, tmp)
    # back across top
    for col in range(right_col_idx-1, left_col_idx-1, -1):
        tmp2 = matrix[top_row_idx][col]
        matrix[top_row_idx][col] = tmp
        tmp = tmp2
    print(matrix, tmp)

def rotate_ring_clockwise(matrix, ring):
    tmp = None
    top_row_idx, bottom_row_idx, left_col_idx, right_col_idx = ring_bounds(
            matrix, ring)
    if top_row_idx is None:
        return

    for col in range(left_col_idx, right_col_idx+1):
        tmp2 = matrix[top_row_idx][col]
        matrix[top_row_idx][col] = tmp
        tmp = tmp2
    for row in range(top_row_idx+1, bottom_row_idx+1):
        tmp2 = matrix[row][right_col_idx]
        matrix[row][right_col_idx] = tmp
        tmp = tmp2
    for col in range(right_col_idx -1, left_col_idx -1):
        tmp2 = matrix[bottom_row_idx][col]
        matrix[bottom_row_idx][col] = tmp
        tmp = tmp2
    for row in range(bottom_row_idx-1, top_row_idx-1):
        tmp2 = matrix[row][left_col_idx]
        matrix[row][left_col_idx] = tmp
        tmp = tmp2

def rotateNcw(matrix, n):
    rings = min(len(matrix)//2, len(matrix[0])//2)

    rots = 0
    while rots < n:
        rots += 1
        for ring in range(rings):
            rotate_ring_counterclockwise(matrix, ring)
    return matrix
