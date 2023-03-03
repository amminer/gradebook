""" Amelia Miner;   BST.py;   6/5/2022
CLASS BST + NODE
Binary search tree without self-balancing and its node.
"""

#~~~~~~~~~~~~~~~~~~~~~~~CLASS TNODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class TNode():
    """ a node in the tree contains references to its parent, children,
    and its data
    """
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
        if isinstance(newLeft, TNode) or newLeft == None:
            self._left = newLeft
        else:
            raise ValueError(f"A {type(newLeft)} is not a TNode!\n")

    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, newRight):
        if isinstance(newRight, TNode) or newRight == None:
            self._right = newRight
        else:
            raise ValueError(f"A {type(newRight)} is not a TNode!\n")

    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, newParent):
        if isinstance(newParent, TNode) or newParent == None:
            self._parent = newParent
        else:
            raise ValueError(f"A {type(newParent)} is not a TNode!\n")

#~~~~~~~~~~~~~~~~~~~END CLASS NODE~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

#~~~~~~~~~~~~~~~~~~~~~~~CLASS BST~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class BST():
    """ stores a collection of nodes; not self-balancing """
    def __init__(self, root=None):
        self._root = root
    
    def __len__(self) -> int:
        return self.lenRecursive(self._root)
    def lenRecursive(self, thisNode:TNode) -> int:
        if not thisNode:
            return 0
        else:
            return 1 \
                 + self.lenRecursive(thisNode.left) \
                 + self.lenRecursive(thisNode.right)

    def display(self):
        """ display the data contained in the tree by inorder traversal """
        self.__displayRecursive(self._root)
    def __displayRecursive(self, thisNode:TNode):
        """ helper for public-facing dispay function """
        if thisNode:
            self.__displayRecursive(thisNode.left)
            print(thisNode.data)
            self.__displayRecursive(thisNode.right)

    def insert(self, newData):
        newNode = TNode(data=newData)
        if not self._root:
            self._root = newNode
        else:
            self.__insertRecursive(self._root, newNode)
    def __insertRecursive(self, thisNode:TNode, newNode:TNode):
        if newNode.data < thisNode.data:
            if thisNode.left:
                self.__insertRecursive(thisNode.left, newNode)
            else:
                thisNode.left = newNode
                newNode.parent = thisNode
        elif newNode.data > thisNode.data:
            if thisNode.right:
                self.__insertRecursive(thisNode.right, newNode)
            else:
                thisNode.right = newNode
                newNode.parent = thisNode
        else: #new == existing data
            # want to pass newData out but don't want to print bulky objects...
            raise ValueError(f"Invalid input! No duplicate values allowed\n")

    def remove(self, key) -> None:
        """ finds and removes a node data matching key if there is one
        raises a ValueError if the key is not found
        """
        if self._root:
            toRemove = self.__findNode(self._root, key)
            if toRemove != None:
                return self.__remove(toRemove)
        raise ValueError(f"Unable to find {key}\n")
    def __remove(self, thisNode:TNode != None) -> None:
        """ internal method for removing a node using a reference to it;
        should only be called by public-facing remove function.
        There are 3 broad cases (2 children, 1 child, and leaf)
        with sub-cases for cases 2 and 3:
        1. In the case that the node has 2 children, swap it with its inorder
        successor and remove the node now that it's a leaf.
        2. In the case that then node has 1 child,
            a. if the node is the tree's root, change the tree's root to be
            the node's child.
            b. if the node is not the root, set the node's child's parent
            attribute to point to the node's parent and set the parent's child
            (left or right) attribute to point to the node's child.
        3. In the case that the root has no children,
            a. if the node is the root, the tree is empty; set root to None.
            b. if the node is not the root, it is a leaf; set the appropriate
            parent pointer to None.
        Finally, in all cases, set the node to None.
        """
        # 1. case two children
        if thisNode.left and thisNode.right:
            inOrderSuccessor = self.__findSmallest(thisNode.right)
            # swap inorder successor with this node
            tempData = inOrderSuccessor.data
            inOrderSuccessor.data = thisNode.data
            thisNode.data = tempData
            self.__remove(inOrderSuccessor)
        # 2. case one child
        elif (thisNode.left and not thisNode.right) or (thisNode.right and not thisNode.left):
            # a. case root
            if thisNode == self._root:
                if thisNode.left:
                    self._root = thisNode.left
                else:
                    self._root = thisNode.right
            # b. case not root
            else:
                if thisNode.left:
                    if thisNode.parent.left == thisNode:
                        thisNode.parent.left = thisNode.left
                    else:
                        thisNode.parent.right = thisNode.left
                    thisNode.left.parent = thisNode.parent
                else:
                    if thisNode.parent.left == thisNode:
                        thisNode.parent.left = thisNode.right
                    else:
                        thisNode.parent.right = thisNode.right
                    thisNode.right.parent = thisNode.parent
            thisNode = None
        # 3. case no children
        else:
            # a. case root
            if thisNode == self._root:
                self._root = None
            # b. case not root (leaf)
            else:
                if thisNode.parent.left == thisNode:
                    thisNode.parent.left = None
                else:
                    thisNode.parent.right = None
            thisNode = None
    def __findSmallest(self, thisNode:TNode):
        """ helper for public facing remove function
        (finds inorder successor)
        """
        if not thisNode.left:
            return thisNode
        else:
            return self.__findSmallest(thisNode.left)

    def lookup(self, key):
        """ finds and returns the data of a node whose data matches key
        if there is one; returns None if the key is not found
        """
        ret = self.__findNode(self._root, key)
        if ret != None:
            return ret.data
        return None

    def __findNode(self, thisNode:TNode, key) -> TNode or None:
        """ helper for public facing remove and lookup functions """
        if not thisNode:
            return None
        elif thisNode.data == key:
            return thisNode
        else:
            ret = self.__findNode(thisNode.left, key)
            if not ret:
                ret = self.__findNode(thisNode.right, key)
            return ret

#~~~~~~~~~~~~~~~~~~~END CLASS BST~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
