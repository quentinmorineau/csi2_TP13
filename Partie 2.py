from Partie1 import Node

class BinaryTree :
    def __init__(self,root):
        self.__root = root

    def getRoot(self):
        return self.__root

    def isRoot(self,node):
        if self.__root == node :
            return True
        else :
            return False

    def size(self, node):
        if node is None:
            return 0
        else:
            return self.size(node.getLeft()) + 1 + self.size(node.getRight())

    def printValues(self, node):
        if node is None:
            return ""
        else:
            return self.printValues(node.getLeft()) + self.printValues(node.getRight()) + " " + str(node.getVal())

    def sumValues(self,node):
        if node is None:
            return 0
        else :
            return self.sumValues(node.getLeft()) + self.sumValues(node.getRight()) + node.getVal()

    def numberLeaves(self,node):
        if node is None :
            return 0
        if node.getRight()==None and node.getLeft()==None :
            return 1
        else :
            return self.numberLeaves(node.getLeft()) + self.numberLeaves(node.getRight())

    def numberInternalNodes(self,node):
        return self.size(node)-self.numberLeaves(node)


    def height(self, node):
        if node is None:
            return -1
        else :
            leftheight = self.height(node.getLeft())
            rightheight = self.height(node.getRight())
            return max(leftheight, rightheight) + 1

    def belongs(self,node,val):
        if node is None:
            return False
        if node.getVal() == val:
            return True
        else:
            return self.belongs(node.getLeft(), val) or self.belongs(node.getRight(), val)

    def ancestors(self,node,val):
        if node is None :
            return False
        if


n3 = Node(3,None,None)
n4 = Node(4,None,n3)
n6 = Node(6,None,None)
n5 = Node(5,n6,n4)
n18 = Node(18,None,None)
n21 = Node(21,None,None)
n19 = Node(19,n21,n18)
n17 = Node(17,n19,None)
n1 = Node(12,n17,n5)
r = BinaryTree(n1)

print(r.isRoot(n1))
print(r.size(n1))
print(r.printValues(n1))
print(r.sumValues(n1))
print(r.numberLeaves(n1))
print(r.numberInternalNodes(n1))
print(r.height(n1))
print(r.belongs(n1,4))
