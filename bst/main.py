import tree
import tree_test

data = [7, 3, 1, 2]
data = [7, 3,]
data = [7,]

t = tree.BST(data)
print(t)
t.print()

def main():
    #test_build_one_node()
    #test_build_two_node()
    #test_build_three_node()
    tree_test.test_print()

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



main()
