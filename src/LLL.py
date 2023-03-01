""" Amelia Miner;   LLL.py;   6/1/2022
CLASS LLL + CLASS NODE
Singly linked linear list and its node.
"""

#~~~~~~~~~~~~~~~~~~~~~~~CLASS NODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Node():
    """ Stores a reference to another node (next) and some data (data) """
    def __init__(self, newData = None):
        self.next = None
        self.data = newData

    def __del__(self):
        self = None

    def __str__(self):
        return str(self.data)
    
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

class LLL():
    """ stores a collection of nodes by managing their "next" references """
    def __init__(self):
        self._head:Node = None
    
    def __str__(self):
        """ returns the contents of the list as a multiline string """
        if not self._head:
            return "Empty\n"
        return self._strRecursive(self._head)
    def _strRecursive(self, head:Node, ret:str = "") -> str:
        """ recursive implementation for stringifying list contents """
        if not head:
            return ret
        else:
            return ret + str(head.data) + '\n' \
                 + self._strRecursive(head.next, ret) + '\n'

    def __len__(self):
        return self._countNodesRecursive(self._head)
    def _countNodesRecursive(self, thisNode:Node) -> int:
        """ recursive implementation for counting nodes """
        if not thisNode:
            return 0
        else:
            return 1 + self._countNodesRecursive(thisNode.next)

    def at(self, index:int):
        """ gets the data of the node at index """
        ret = self._getAtRecursive(self._head, index)
        if type(ret) == bool and not ret:
            raise IndexError(f"Index {index} out of range!\n")
        return ret
    def _getAtRecursive(self, thisNode:Node, index:int):
        """ recursive implementation for finding list item at index """
        if not thisNode or index < 0:
            return False
        elif index == 0:
            return thisNode.data
        else:
            return self._getAtRecursive(thisNode.next, index - 1)

    def pushBack(self, newData):
        """ appends a data item to the list """
        if not self._head:
            self._head = Node(newData)
        else:
            self._pushBackRecursive(self._head, newData)
    def _pushBackRecursive(self, thisNode:Node, newData):
        """ recursive implementation for appending a node to the list
        MUST not be called with thisNode=None
        """
        if not thisNode.next:
            thisNode.next = Node(newData)
        else:
            self._pushBackRecursive(thisNode.next, newData)

    def remove(self, key):
        """ removes a node from the list if one can be found whose data
        matches the provided key
        """
        thatPrev, thatOne = self._findPairRecursive(self._head, key)
        if type(thatOne) == bool and type(thatPrev) == bool \
        and not thatOne and not thatPrev:
            raise ValueError(f"{key} was not found\n")
        else:
            self._remove(thatPrev, thatOne)
    def _findPairRecursive(self, thisNode:Node, key):
        """ recursive implementation for finding a node by key
        also keeps track of the previous node to reconnect list on removal
        """
        # case head matches
        if not thisNode:
            return False, False
        elif thisNode == self._head and thisNode.data == key:
            return None, thisNode
        # case match after head
        elif thisNode.next and thisNode.next.data == key:
            return thisNode, thisNode.next
        else:
            return self._findPairRecursive(thisNode.next, key)
    def _remove(self, thatPrev:Node, thatNode:Node):
        """ removes thatNode and reconnects the list around it
        thatPrev may be None!
        """
        if not thatPrev:            #case head
            self._head = thatNode.next
        elif not thatNode.next:     #case tail
            thatPrev.next = None
        else:                       #case sandwiched
            thatPrev.next = thatNode.next
        del thatNode # unsure if this is necessary...

    def lookup(self, key):
        """ finds a node in the list according to its data == key 
        returns None if node cannot be found
        """
        ret:Node = self._findRecursive(self._head, key)
        return ret
    def _findRecursive(self, thisNode:Node, key):
        """ recursive implementation for finding a node """
        if not thisNode:
            return None
        elif thisNode.data == key:
            return thisNode.data
        else:
            return self._findRecursive(thisNode.next, key)
