import imp
import __init__
from random import randint
from LLL import Node
ns = [Node() for _ in range(1000)]

def test_next():
    for n in ns:
        n.next = ns[randint(0, len(ns)-1)]
        assert n.next != None

#No need to test data since no filtering?...