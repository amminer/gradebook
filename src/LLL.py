from glob import escape

#~~~~~~~~~~~~~~~~~~~~~~~CLASS NODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Node():
    def __init__(self):
        self.next = None
        self.data = None

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
    
    def __str__(self, ret:str = ""):
        return self.strRecursive(self.head)

    def strRecursive(self, head:Node, ret:str = ""):
        if not self.head: #head is not None; None is falsy
            return ret
        else:
            return '\n'.join(ret,
                             str(self.head.data),
                             self.strRecursive(head.next, ret))

    #TODO def pushBack(self):

    #TODO def remove(self):

    #TODO def lookup(self):