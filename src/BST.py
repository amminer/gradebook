""" Amelia Miner;   BST.py;   6/5/2022
CLASS BST + NODE
Binary search tree without self-balancing and its node.
"""

#~~~~~~~~~~~~~~~~~~~~~~~CLASS NODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Node():
    """ a node in the tree contains references to its parent, children, and its data """
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        """ dump node contents to console for debugging """
        ld, rd = None, None
        if self.left:
            ld = self.left.data
        if self.right:
            rd = self.right.data
        return str(self.data) + f"LEFT: {ld}, RIGHT: {rd}"

    @property
    def data(self):
        return self._data
    @data.setter
    def data(self, newData):
        self._data = newData

    @property
    def left(self):
        return self._left
    @left.setter
    def left(self, newLeft):
        if isinstance(newLeft, Node) or newLeft == None:
            self._left = newLeft
        else:
            raise ValueError(f"A {type(newLeft)} is not a Node!\n")

    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, newRight):
        if isinstance(newRight, Node) or newRight == None:
            self._right = newRight
        else:
            raise ValueError(f"A {type(newRight)} is not a Node!\n")

    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, newParent):
        if isinstance(newParent, Node) or newParent == None:
            self._parent = newParent
        else:
            raise ValueError(f"A {type(newParent)} is not a Node!\n")

#~~~~~~~~~~~~~~~~~~~END CLASS NODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~CLASS BST~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class BST():
    """ stores a collection of nodes; not self-balancing """
    def __init__(self, root=None):
        self._root = root
    
    def __len__(self) -> int:
        return self.lenRecursive(self._root)
    def lenRecursive(self, root:Node) -> int:
        if not root:
            return 0
        else:
            return 1 \
                 + self.lenRecursive(root.left) \
                 + self.lenRecursive(root.right)

    def display(self):
        """ display the data contained in the tree by inorder traversal """
        self.__displayRecursive(self._root)
    def __displayRecursive(self, root:Node):
        """ helper for public-facing dispay function """
        if root:
            self.__displayRecursive(root.left)
            print(root.data)
            self.__displayRecursive(root.right)

    def insert(self, newData):
        newNode = Node(data=newData)
        if not self._root:
            self._root = newNode
        else:
            self.__insertRecursive(self._root, newNode)
    def __insertRecursive(self, root:Node, newNode:Node):
        if newNode.data < root.data:
            if root.left:
                self.__insertRecursive(root.left, newNode)
            else:
                root.left = newNode
                newNode.parent = root
        elif newNode.data > root.data:
            if root.right:
                self.__insertRecursive(root.right, newNode)
            else:
                root.right = newNode
                newNode.parent = root
        else: #new == existing data
            #want to pass newData out but don't want to print bulky objects...
            raise ValueError(f"Invalid input! No duplicate values are allowed\n")

    def remove(self, key) -> None:
        """ finds and removes a node data matching key if there is one
        raises a ValueError if the key is not found
        """
        if self._root:
            toRemove = self.__findNode(self._root, key)
            if toRemove != None:
                return self.__remove(toRemove)
        raise ValueError(f"Unable to find {key}\n")
    #removes a node using a reference to it
    #do not call with None
    def __remove(self, root:Node != None) -> None:
        if root.left and root.right: # case 2 children
            inOrderSuccessor = self.__findSmallest(root.right)
            #swap inorder successor with this node and recurse 
            tempData = inOrderSuccessor.data
            inOrderSuccessor.data = root.data
            root.data = tempData
            self.__remove(inOrderSuccessor)
        elif (root.left and not root.right) or (root.right and not root.left): #case 1 c
            if root == self._root: #case root
                if root.left:
                    self._root = root.left
                else:
                    self._root = root.right
            else: #case not root
                if root.left:
                    if root.parent.left == root:
                        root.parent.left = root.left
                    else:
                        root.parent.right = root.left
                    root.left.parent = root.parent
                else:
                    if root.parent.left == root:
                        root.parent.left = root.right
                    else:
                        root.parent.right = root.right
                    root.right.parent = root.parent
            root = None
        else: #case no children
            if root == self._root: #case root
                self._root = None
            else: #case not root (leaf)
                if root.parent.left == root:
                    root.parent.left = None
                else:
                    root.parent.right = None
            root = None
    def __findSmallest(self, root:Node):
        """ helper for public facing remove function (helps to find inorder successor) """
        if not root.left:
            return root
        else:
            return self.__findSmallest(root.left)

    def lookup(self, key):
        """ finds and returns the data of a node whose data matches key
        if there is one; returns None if the key is not found
        """
        ret = self.__findNode(self._root, key)
        if ret != None:
            return ret.data
        return None

    def __findNode(self, root:Node, key) -> Node or None:
        """ helper for public facing remove and lookup functions """
        if not root:
            return None
        elif root.data == key:
            return root
        else:
            ret = self.__findNode(root.left, key)
            if not ret:
                ret = self.__findNode(root.right, key)
            return ret

#~~~~~~~~~~~~~~~~~~~END CLASS BST~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
