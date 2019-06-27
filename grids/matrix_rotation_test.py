import matrix_rotation

case_1 = [
    [1, 2, 3, 4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],]
expt_1_rot2 = [
    [3,4,8,12],
    [2,11,10,16],
    [1,7,6,15],
    [5,9,13,14],]

def test_ring_bounds():
    matrix = [[1,2],[4,3]]
    a,b,c,d = matrix_rotation.ring_bounds(matrix, 0)
    assert a ==0
    assert b ==1
    assert c ==0
    assert d ==1

def test_rot_ring_ccw():
    matrix = [[1,2],[4,3]]
    matrix_rotation.rotate_ring_counterclockwise(matrix, 0)
    assert matrix == [[2,3],[1,4]]

    matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9]]
    matrix_rotation.rotate_ring_counterclockwise(matrix, 0)
    assert matrix == [
            [2,3,6],
            [1,5,9],
            [4,7,8]]
    matrix = [
        [1,2,3,4],
        [5,6,7,8],
        [9,10,11,12],
        [13,14,15,16],]
    matrix_rotation.rotate_ring_counterclockwise(matrix, 1)
    assert matrix == [
        [1,2,3,4],
        [5,7,11,8],
        [9,6,10,12],
        [13,14,15,16],]

def test_rotate_skinny():
    matrix = [
            [1,2,3],
            [4,5,6],
            [7,8,9],
            [10,11,12],
            ]
    matrix_rotation.rotateNcw(matrix, 1)
    assert matrix == [
            [2,3,6],
            [1,5,9],
            [4,8,12],
            [7,10,11],
            ]

def test_rotate_cw():
    matrix_rotation.rotateNcw(case_1, 2)
    assert case_1 == expt_1_rot2
