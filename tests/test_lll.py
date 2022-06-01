import __init__
from random import randint
from LLL import LLL

def test_init_str():
    l = LLL()
    assert not l #empty LLL is falsy
    assert l.head == None
    assert l.__str__() == "List is empty"

#also tests __len__
def test_pushBack():
    l = LLL()
    assert not l #empty LLL is falsy
    l.pushBack("First thing")
    assert l #non-empty is truthy
    assert len(l) == 1
    l.pushBack("Another thing")
    assert len(l) == 2

def test_at():
    l = LLL()
    l.pushBack("a")
    l.pushBack("b")
    assert l.at(0) == "a"
    assert l.at(1) == "b"
    try:
        l.at(2)
        assert False #should raise IE
    except IndexError as ie:
        print(ie)
        assert True
    try:
        l.at(-5)
        assert False #should raise IE
    except IndexError as ie:
        print(ie)
        assert True
    
def remove(self):
    pass #TODO

def lookup(self):
    pass #TODO

"""
if __name__ == "__main__":
    test_at()
"""