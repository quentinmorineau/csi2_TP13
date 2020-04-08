from Partie1 import Node

class BinaryTree :
    def __init__(self,root):
        self.__root = root

    def getRoot(self):
        return self.__root

r = BinaryTree(12)
n_root = Node(r.getRoot(),17,5)
n1_left = Node(n_root.getLeft(),4,6)
n2_left_left = Node(n1_left.getLeft(),None,3)
n2_right = Node(n_root.getRight(),19,None)
n3 = Node(n2_right.getRight(),21,18)


