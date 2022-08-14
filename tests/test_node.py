import __init__
from random import randint
from LLL import Node
import BST

""" Amelia Miner;   test_node.py;  6/1/2022 """

def test_next():
    ns = [Node() for _ in range(1000)]
    for n in ns:
        n.next = ns[randint(0, len(ns)-1)]
        assert n.next != None

def test_data_lll():
    ns = [Node() for _ in range(1000)]
    for n in ns:
        n.data = randint(0,1000)
    assert all([n.data != None for n in ns])

def test_data_constr_lll():
    newNode = Node("some data")
    assert newNode.data == "some data"

def test_ptrs():
    ns = [BST.Node() for _ in range(1000)]
    for n in ns:
        n.left = ns[randint(0, len(ns)-1)]
        n.right = ns[randint(0, len(ns)-1)]
        n.parent = ns[randint(0, len(ns)-1)]
        assert n.left != None
        assert n.right != None
        assert n.parent != None

def test_data_bst():
    ns = [BST.Node() for _ in range(1000)]
    for n in ns:
        n.data = randint(0,1000)
    assert all([n.data != None for n in ns])

def test_data_constr_bst():
    newNode = BST.Node("some data")
    assert newNode.data == "some data"