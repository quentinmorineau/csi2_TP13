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
        else :
            return self.numberLeaves()

n3 = Node(3,None,None)
n4 = Node(4,None,n3)
n6 = Node(6,None,None)
n5 = Node(5,n6,n4)
n18 = Node(18,None,None)
n21 = Node(21,None,None)
n19 = Node(19,n21,n18)
n17 = Node(17,n19,None)
n1 = Node(12,n17,n5)
Racine = BinaryTree(n1)

print(Racine.isRoot(n1))
print(Racine.size(n1))
print(Racine.printValues(n1))
print(Racine.sumValues(n1))
