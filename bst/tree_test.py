import tree

def test_build_one_node():
    oneNodeTree = tree.BST([7])
    assert oneNodeTree._root is not None
    assert oneNodeTree._root.val == 7

def test_build_two_node():
    print("testing Left tree")
    twoNodeTreeLeft = tree.BST([7, 3])
    assert twoNodeTreeLeft._root is not None
    assert twoNodeTreeLeft._root.val == 7
    assert twoNodeTreeLeft._root.right is None
    assert twoNodeTreeLeft._root.left is not None
    assert twoNodeTreeLeft._root.left.val == 3

    print("testing Right tree")
    twoNodeTreeRight = tree.BST([7, 11])
    assert twoNodeTreeRight._root is not None
    assert twoNodeTreeRight._root.val == 7
    assert twoNodeTreeRight._root.right is not None
    assert twoNodeTreeRight._root.right.val == 11


def test_build_three_node():
    print("testing Left tree")
    threeNodeTree = tree.BST([7, 3, 4])
    assert threeNodeTree._root is not None
    assert threeNodeTree._root.val == 7
    assert threeNodeTree._root.right is None
    assert threeNodeTree._root.left is not None
    assert threeNodeTree._root.left.val == 3
    assert threeNodeTree._root.left.left is None
    assert threeNodeTree._root.left.right is not None
    assert threeNodeTree._root.left.right.val == 4

def test_inorder():
    data = [7, 3, 4, 1, 2, 11, 9 , 12]
    bst = tree.BST(data)
    assert bst.inorder() == sorted(data)

def test_to_string():
    data = [7, 3, 4, 1, 2, 11, 9 , 12]
    bst = tree.BST(data)
    assert bst.to_string() == ",".join([str(ii) for ii in sorted(data)])

"""
            7
    3               11
1      4        9       12
  2
"""
def test_preorder():
    data = [7, 3, 4, 1, 2, 11, 9 , 12]
    exp = [7, 3, 1, 2, 4, 11, 9, 12]

    acc = []
    def op(val):
        acc.append(val)
    bst = tree.BST(data)
    bst._preorder(op)
    assert acc == exp
def test_preorder():
    data = [7, 3, 4, 1, 2, 11, 9 , 12]
    exp = [2,1,4,3,9,12,11,7]
    acc = []
    def op(val):
        acc.append(val)
    bst = tree.BST(data)
    bst._postorder(op)
    assert acc == exp

def test_breadthfirst():
    data = [7, 3, 4, 1, 2, 11, 9 , 12]
    exp = [7, 3, 11, 1, 4, 9, 12, 2]
    acc = []
    def op(val):
        acc.append(val)
    bst = tree.BST(data)
    bst._levelorder(op)
    assert acc == exp
