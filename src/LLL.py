#~~~~~~~~~~~~~~~~~~~~~~~CLASS NODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Node():
    def __init__(self, newData = None):
        self.next = None
        self.data = newData

    def __str__(self):
        return self.data
    
    @property
    def next(self):
        return self._next
    
    @next.setter
    def next(self, newNext):
        if type(newNext) != Node and newNext != None:
            raise ValueError("Node.next must be a Node")
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
    def __init__(self):
        self.head:Node = None
    
    def __str__(self):
        if not self.head:
            return "List is empty"
        return self._strRecursive(self.head)
    def _strRecursive(self, head:Node, ret:str = "") -> str:
        if not self.head: #head is not None; None is falsy
            return ret
        else:
            return '\n'.join(ret,
                             str(self.head.data),
                             self.strRecursive(head.next, ret))

    def __len__(self):
        return self._countNodes(self.head)
    def _countNodes(self, thisNode:Node) -> int:
        if not thisNode:
            return 0
        else:
            return 1 + self._countNodes(thisNode.next)

    #should do __getitem__, but don't want to deal with multiple returns yet
    def at(self, index:int): #returns Node's data type...
        ret = self.getAtRecursive(index, self.head)
        if not ret:
            raise IndexError(f"Index {index} out of range!")
        return ret
    def getAtRecursive(self, index:int, thisNode:Node):
        if not thisNode or index < 0:
            return False
        elif index == 0:
            return thisNode.data
        else:
            return self.getAtRecursive(index - 1, thisNode.next)


    def pushBack(self, newData):
        if not self.head:
            self.head = Node(newData)
        else:
            self._pushBackRecursive(self.head, newData)
    #DO NOT CALL WITH NULL thisNode
    def _pushBackRecursive(self, thisNode:Node, newData):
        if not thisNode.next:
            thisNode.next = Node(newData)
        else:
            self.pushBackRecursive(thisNode.next, newData)

    #TODO def remove(self):

    #TODO def lookup(self):