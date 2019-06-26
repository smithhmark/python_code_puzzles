from collections import deque

class Node():
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

class BST():
    def __init__(self, vals=None):
        self._root = None
        if vals is not None:
            for val in vals:
                #print("inserting ", val)
                self.insert(val)

    def insert(self, val):
        if self._root is None:
            self._root = Node(val)
        else:
            cur = self._root
            while cur != None:
                if val < cur.val:
                    if cur.left is None:
                        cur.left = Node(val)
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right is None:
                        cur.right = Node(val)
                        break
                    else:
                        cur = cur.right

    def to_string(self):
        accum = []
        def op(val):
            accum.append(val)
        self._inorder(op)
        return ",".join(str(ii) for ii in accum)

    def inorder(self):
        accum = []
        def op(val):
            accum.append(val)
        self._inorder(op)
        return accum

    def _inorder(self, op):
        stack = []
        if self._root is not None:
            stack.append((self._root, None))
        while len(stack) != 0:
            #print(','.join([str(ii.val) for ii in stack]))
            # descend left
            # "visit"
            # descend right
            node, val  = stack.pop()
            if node is not None:
                if node.right is not None:
                    stack.append((node.right, None))
                stack.append((None, node.val))
                if node.left is not None:
                    stack.append((node.left, None))
            else:
                op(val)

    def _preorder(self, op):
        stack = []
        if self._root is not None:
            stack.append((self._root, None))
        while len(stack) != 0:
            #print(','.join([str(ii.val) for ii in stack]))
            # "visit"
            # descend left
            # descend right
            node, val  = stack.pop()
            if node is not None:
                if node.right is not None:
                    stack.append((node.right, None))
                if node.left is not None:
                    stack.append((node.left, None))
                stack.append((None, node.val))
            else:
                op(val)

    def _postorder(self, op):
        stack = []
        if self._root is not None:
            stack.append((self._root, None))
        while len(stack) != 0:
            #print(','.join([str(ii.val) for ii in stack]))
            # descend left
            # descend right
            # "visit"
            node, val  = stack.pop()
            if node is not None:
                stack.append((None, node.val))
                if node.right is not None:
                    stack.append((node.right, None))
                if node.left is not None:
                    stack.append((node.left, None))
            else:
                op(val)
    def _levelorder(self, op):
        qq = deque()
        if self._root is not None:
            qq.append(self._root)

        while len(qq) > 0:
            node = qq.popleft()
            op(node.val)
            if node.left is not None:
                qq.append(node.left)
            if node.right is not None:
                qq.append(node.right)
