import string

class Null:
    state = "Null"
    printable = " "
    weight = ""
    ID =""

class Link:
    state = "link"
    Deleted = False
    printable = "+"
    weight = 0
    ID = int
    node1 = string
    node2 = string
    def __init__(self,ID,  row, column,node1,node2,type):
        self.ID=ID
        self.r=row
        self.c=column
        self.node1=node1
        self.node2=node2
        if (type == True):
            self.printable = "-"
        else:
            self.printable = "|"



class Node:
    manhattan = 0
    combinedweight = 0
    state = "node"
    printable = "*"
    weight = "*"
    ID = int
    parentID = int
    depth = int

    def __init__(self,ID,  row, column):
        self.ID=ID
        self.r=row #rows and columns for FULLARRAY!!
        self.c=column

