from Student import Student

class Node():pass #declaration so BST can come first

class BST():
    def __init__(self, root=None):
        self.root = root
    
    @property
    def root(self):
        return self._root
    @root.setter
    def root(self, newRoot):
        if isinstance(newRoot, Node) or newRoot == None:
            self._root = newRoot
        else:
            raise ValueError(f"A {type(newRoot)} is not a Node!")

    def display(self):
        self.displayRecursive(self.root)
    def displayRecursive(self, root:Node):
        if root: #inorder traversal
            self.displayRecursive(root.left)
            print(root.data)
            self.displayRecursive(root.right)

    def insert(self, newData):
        newNode = Node(data=newData)
        if not self.root:
            self.root = newNode
        else:
            self.insertRecursive(self.root, newNode)
    def insertRecursive(self, root:Node, newNode:Node):
        if newNode.data <= root.data:
            if root.left:
                self.insertRecursive(root.left, newNode)
            else:
                root.left = newNode
                newNode.parent = root
        else: #newData > root.data
            if root.right:
                self.insertRecursive(root.right, newNode)
            else:
                root.right = newNode
                newNode.parent = root

class Node():
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

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
            raise ValueError(f"A {type(newLeft)} is not a Node!")

    @property
    def right(self):
        return self._right
    @right.setter
    def right(self, newRight):
        if isinstance(newRight, Node) or newRight == None:
            self._right = newRight
        else:
            raise ValueError(f"A {type(newRight)} is not a Node!")

    @property
    def parent(self):
        return self._parent
    @parent.setter
    def parent(self, newParent):
        if isinstance(newParent, Node) or newParent == None:
            self._parent = newParent
        else:
            raise ValueError(f"A {type(newParent)} is not a Node!")
