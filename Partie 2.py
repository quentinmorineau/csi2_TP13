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




n12 = Node(12,17,5)
r = BinaryTree(n12)
n5 = Node(n12.getLeft(),6,4)
n4 = Node(n5.getLeft(),None,3)
n3 = Node(n4.getLeft(),None,None)
n6 = Node(n5.getRight(),None,None)
n17 = Node(n12.getRight(),19,None)
n19 = Node(n17.getRight(),21,18)
n18 = Node(n19.getLeft(),None,None)
n21 = Node(n19.getRight(),None,None)

#print(r.isRoot(n5))
#r.size(n12)
r.printValues(n12)
