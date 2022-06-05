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

def t_display():
    t = test_insert(True)
    t.display()

if __name__ == "__main__":
    t_display()