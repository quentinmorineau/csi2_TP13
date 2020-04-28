class Node:
    def __init__(self,val,right,left):
        self.__v = val
        self.__r = right
        self.__l = left

    def getVal(self):
        return self.__v

    def getRight(self):
        return self.__r

    def getLeft(self):
        return self.__l

    def setRight(self,r):
        self.__r = r

    def setLeft(self,l):
        self.__l = l

    def __str__(self):
        return "La valeur du noeud est : "+str(self.__v)

n1 = Node(12,17,5)
n2 = Node(4,6,8)
#print(n2)
