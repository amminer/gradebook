""" Amelia Miner;   BST.py;   6/5/2022
CLASS BST + NODE
Binary search tree without self-balancing and its node.
"""

#~~~~~~~~~~~~~~~~~~~~~~~CLASS NODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Node():
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self): #DEBUG
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

    """ not appropriate here, I think
    @property
    def root(self):
        return self._root
    @root.setter
    def root(self, newRoot):
        if isinstance(newRoot, Node) or newRoot == None:
            self._root = newRoot
        else:
            raise ValueError(f"A {type(newRoot)} is not a Node!\n")
    """

    def display(self):
        self.displayRecursive(self._root)
    def displayRecursive(self, root:Node):
        if root: #inorder traversal
            self.displayRecursive(root.left)
            print(root.data)
            self.displayRecursive(root.right)

    def insert(self, newData):
        newNode = Node(data=newData)
        if not self._root:
            self._root = newNode
        else:
            self.insertRecursive(self._root, newNode)
    def insertRecursive(self, root:Node, newNode:Node):
        if newNode.data < root.data:
            if root.left:
                self.insertRecursive(root.left, newNode)
            else:
                root.left = newNode
                newNode.parent = root
        elif newNode.data > root.data:
            if root.right:
                self.insertRecursive(root.right, newNode)
            else:
                root.right = newNode
                newNode.parent = root
        else: #new == existing data
            #want to pass newData out but don't want to print bulky objects...
            raise ValueError(f"Invalid input! No duplicate values are allowed\n")

    #finds and removes a node with key data if there is one
    def remove(self, key) -> None: #may raise ValueError
        if self._root:
            toRemove = self._findNode(self._root, key)
            if toRemove != None:
                return self._remove(toRemove)
        raise ValueError(f"Unable to find {key}\n")
    def _findNode(self, root:Node, key) -> Node or None:
        if not root:
            return None
        elif root.data == key:
            return root
        else:
            ret = self._findNode(root.left, key)
            if not ret:
                ret = self._findNode(root.right, key)
            return ret
    #removes a node using a reference to it
    #do not call with None
    def _remove(self, root:Node != None) -> None:
        if root.left and root.right: # case 2 children
            #find the in-order successor
            inOrderSuccessor = self._findSmallest(root.right)
            #assert inOrderSuccessor != None #DEBUG
            #assert not (inOrderSuccessor.left and inOrderSuccessor.right)
            #swap it with this node and recurse 
            tempData = inOrderSuccessor.data
            inOrderSuccessor.data = root.data
            root.data = tempData
            self._remove(inOrderSuccessor)
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
    def _findSmallest(self, root:Node):
        if not root.left:
            return root
        else:
            return self._findSmallest(root.left)

    def lookup(self, key): #returns None or datatype
        ret = self._findNode(self._root, key)
        if ret != None:
            return ret.data
        return None

#~~~~~~~~~~~~~~~~~~~END CLASS BST~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
