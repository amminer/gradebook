import __init__
from BST import Node, BST

def test_nodeSetters():
    a = Node(data=1)
    b = Node(data=2)
    c = Node(data=3)
    d = "bread"
    e = 4
    a.left = b
    b.right = c
    c.parent = a #graph time
    assert a.left == b
    assert a.right == None
    assert a.left.right.parent == a
    try:
        a.right = d
        assert False
    except ValueError:
        assert True
    try:
        c.right = e
        assert False
    except ValueError:
        assert True

def test_insert(ret:bool=False):
    t = BST()
    t.insert(5)
    t.insert(3)
    t.insert(7)
    assert t.root.data == 5
    assert t.root.left.data == 3
    assert t.root.right.data == 7
    assert t.root.left.parent == t.root
    assert t.root.right.parent == t.root
    t.insert(6)
    assert t.root.right.left.data == 6
    t.insert(9)
    t.insert(10)
    t.insert(11)
    assert t.root.right.right.right.right.data == 11 #not balanced
    if ret:
        return t

def test_len():
    t = BST()
    assert len(t) == 0
    t.insert(5)
    assert len(t) == 1
    t.insert(3)
    assert len(t) == 2
    t.insert(7)
    assert len(t) == 3
    t.insert(6)
    assert len(t) == 4
    t.insert(9)
    assert len(t) == 5
    t.insert(4)
    assert len(t) == 6

def test_removeLeaf():
    #       5
    #   3       7
    #     4   6   9
    t = BST()
    t.insert(5)
    t.insert(3)
    t.insert(7)
    t.insert(6)
    t.insert(9)
    t.insert(4)
    t.remove(4)
    assert len(t) == 5
    assert t.root.data == 5
    assert t.root.left.data == 3 and not t.root.left.right \
                            and not t.root.left.left
    assert t.root.right.right.data == 9 \
       and t.root.right.left.data == 6

def test_removeParentOfOneRightChild():
    #       5
    #   3       7
    #     4   6   9
    t = BST()
    t.insert(5)
    t.insert(3)
    t.insert(7)
    t.insert(6)
    t.insert(9)
    t.insert(4)
    t.remove(3)
    assert len(t) == 5
    assert t.root.data == 5
    assert t.root.left.data == 4 and not t.root.left.right \
                            and not t.root.left.left
    assert t.root.right.right.data == 9 \
       and t.root.right.left.data == 6

def test_removeParentOfOneLeftChild():
    #       5
    #   3       7
    # 2       6   9
    t = BST()
    t.insert(5)
    t.insert(3)
    t.insert(7)
    t.insert(6)
    t.insert(9)
    t.insert(2)
    t.remove(3)
    assert len(t) == 5
    assert t.root.data == 5
    assert t.root.left.data == 2 and not t.root.left.right \
                            and not t.root.left.left
    assert t.root.right.right.data == 9 \
       and t.root.right.left.data == 6

def test_removeParentOfTwo():
    #       5
    #   3       7
    # 2       6   9
    t = BST()
    t.insert(5)
    t.insert(3)
    t.insert(7)
    t.insert(6)
    t.insert(9)
    t.insert(2)
    t.remove(7)
    assert len(t) == 5
    assert t.root.data == 5
    assert t.root.left.data == 3 and not t.root.left.right \
                            and t.root.left.left.data == 2
    assert t.root.right.data == 9 \
       and t.root.right.left.data == 6 \
       and not t.root.right.right

def test_removeRoot_leaf():
    #       5
    t = BST()
    t.insert(5)
    t.remove(5)
    assert t.root == None
    assert not t
    assert len(t) == 0

def test_removeRoot_oneChild():
    #       5
    #   3
    t = BST()
    t.insert(5)
    t.insert(3)
    t.remove(5)
    assert len(t) == 1
    assert t.root.data == 3

def test_removeRootTwoChildren():
    #       5
    #   3       7
    t = BST()
    t.insert(5)
    t.insert(3)
    t.insert(7)
    t.remove(5)
    assert len(t) == 2
    assert t.root.data == 7
    assert t.root.left.data == 3 and not t.root.right

def test_lookup():
    #       5
    #   3       7
    # 2       6   9
    t = BST()
    t.insert(5)
    t.insert(3)
    t.insert(7)
    t.insert(6)
    t.insert(9)
    t.insert(2)
    assert t.lookup(5) == 5
    assert t.lookup(2) == 2
    assert t.lookup(3) == 3
    assert t.lookup(7) == 7
    assert t.lookup(4) == None
    assert t.lookup("6") == None #invalid data type

def t_display():
    t = test_insert(True)
    t.display()

if __name__ == "__main__":
    test_remove_leaf()