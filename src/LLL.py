""" Amelia Miner;   LLL.py;   6/1/2022
CLASS LLL + CLASS NODE
Singly linked linear list and its node.
"""

#~~~~~~~~~~~~~~~~~~~~~~~CLASS NODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Node():
    def __init__(self, newData = None):
        self.next = None
        self.data = newData

    def __del__(self):
        self = None

    def __str__(self):
        return self.data
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, newNext):
        if type(newNext) != Node and newNext != None:
            raise ValueError("Node.next must be a Node.\n")
        else:
            self._next = newNext

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, newData):
        self._data = newData

#~~~~~~~~~~~~~~~~~~~END CLASS NODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~#



#~~~~~~~~~~~~~~~~~~~~~~~CLASS LLL~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#I want to make this iterable but don't really have time to learn that :(
#Would be nice to be able to use it in list comprehensions

class LLL():
    def __init__(self):
        self._head:Node = None
    
    def __str__(self):
        if not self._head:
            return "Empty\n"
        return self._strRecursive(self._head)
    def _strRecursive(self, head:Node, ret:str = "") -> str:
        if not head: #head is not None; None is falsy
            return ret
        else:
            return ret + str(head.data) + '\n' \
                 + self._strRecursive(head.next, ret) + '\n'

    def __len__(self):
        return self._countNodesRecursive(self._head)
    def _countNodesRecursive(self, thisNode:Node) -> int:
        if not thisNode:
            return 0
        else:
            return 1 + self._countNodesRecursive(thisNode.next)

    #should do __getitem__, but don't want to deal with multiple returns yet
    def at(self, index:int): #returns Node's data type...
        ret = self._getAtRecursive(self._head, index)
        if type(ret) == bool and not ret: #don't want to accidentally
            raise IndexError(f"Index {index} out of range!\n") #catch falsy
        return ret
    def _getAtRecursive(self, thisNode:Node, index:int):
        if not thisNode or index < 0:
            return False
        elif index == 0:
            return thisNode.data
        else:
            return self._getAtRecursive(thisNode.next, index - 1)

    def pushBack(self, newData):
        if not self._head:
            self._head = Node(newData)
        else:
            self._pushBackRecursive(self._head, newData)
    #DO NOT CALL WITH NULL thisNode
    def _pushBackRecursive(self, thisNode:Node, newData):
        if not thisNode.next:
            thisNode.next = Node(newData)
        else:
            self._pushBackRecursive(thisNode.next, newData)

    def remove(self, key):
        thatPrev, thatOne = self._findPairRecursive(self._head, key)
        if type(thatOne) == bool and type(thatPrev) == bool \
           and not thatOne and not thatPrev:
            raise ValueError(f"{key} was not found\n")
        else:
            self._remove(thatPrev, thatOne)
    def _findPairRecursive(self, thisNode:Node, key):
        #case head matches
        if not thisNode:
            return False, False
        elif thisNode == self._head and thisNode.data == key:
            return None, thisNode
        #case match after head
        elif thisNode.next and thisNode.next.data == key:
            return thisNode, thisNode.next
        else:
            return self._findPairRecursive(thisNode.next, key)
    #thatPrev may == None
    def _remove(self, thatPrev:Node, thatNode:Node):
        if not thatPrev:            #case head
            self._head = thatNode.next
        elif not thatNode.next:     #case tail
            thatPrev.next = None
        else:                       #case sandwiched
            thatPrev.next = thatNode.next
        del thatNode #is this needed?

    def lookup(self, key): #returns node data type or None
        ret:Node = self._findRecursive(self._head, key)
        return ret
    def _findRecursive(self, thisNode:Node, key):
        if not thisNode:
            return None
        elif thisNode.data == key:
            return thisNode.data
        else:
            return self._findRecursive(thisNode.next, key)
