import __init__
from random import randint
from LLL import Node

def test_next():
    ns = [Node() for _ in range(1000)]
    for n in ns:
        n.next = ns[randint(0, len(ns)-1)]
        assert n.next != None

def test_data():
    ns = [Node() for _ in range(1000)]
    for n in ns:
        n.data = randint(0,1000)
    assert all([n.data != None for n in ns])

def test_data_constr():
    newNode = Node("some data")
    assert newNode.data == "some data"