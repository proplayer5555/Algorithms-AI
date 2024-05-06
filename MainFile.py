from NodeLink import Node
from NodeLink import Link
from NodeLink import Null
from UCS import ucs
from ASTAR import astar
from manhattan import manhattan
from IDS import ids
import random
from timeit import default_timer as timer



nSTR = input("Insert n: ")
percentageSTR = input("Insert removed link percentage (%): ")
n=int(nSTR)
percentage=int(percentageSTR)

FullArray = [[Null for x in range(2*n-1)] for x in range(2*n-1)]
NodeArray = [[Null for x in range(n)] for x in range(n)]

LinkID=0 #using link ID to count
for r in range(n):
    #Create first horizontal Node-Link-Node-Link
    for c in range(n):
        #Insert Node
        nodeA = Node(c + r * n, 2*r, 2*c)
        FullArray[2*r][2*c] = nodeA
        NodeArray[r][c] = nodeA
        if (c!=n-1):
            #link(ID link,row,column,prevNODE,nextNODE,horizontal or vertical)
            linkA = Link(LinkID, 2*r,(2 * c)+1,c + r * n,c +1 + r * n,True)
            LinkID+=1
            linkA.weight = random.randint(1,20)
            FullArray[2*r][(2 * c)+1] = linkA
    #Create second horizontal Link-nothing-Link-Nothing
    if (r!=n-1):
        for c in range(n):
            #Insert Link
            linkA = Link(LinkID,2*r+1,2*c,c + (r-1) * n,c + (r+1) * n,False)
            LinkID+=1
            linkA.weight = random.randint(1,20)
            FullArray[2*r+1][2*c] = linkA

#---------------------------------------------------------------------
counter = int((percentage/100)*(2*n*(n-1)))


#remove links
while(counter>0):
    randomR = random.randint(0,2*n-2)
    randomC = random.randint(0,2*n-2)
    temp = FullArray[randomR][randomC]
    if (temp.weight != "" and temp.weight != "*"):
        if (temp.Deleted != True):
            FullArray[randomR][randomC].Deleted = True
            FullArray[randomR][randomC].printable = " "
            #print("Link ",temp.ID," removed")
            counter-=1


#setup start and end nodes
startID = random.randint(0,n*n-1)
print("start ID selected ",startID)
for r in range(2*n-1):
    for c in range(2*n-1):
        if (FullArray[r][c].state == "node" and FullArray[r][c].ID == startID):
            FullArray[r][c].state = "start"
            FullArray[r][c].printable = "o"
            FullArray[r][c].depth = 0 # setup iteration number
            FullArray[r][c].parentID = FullArray[r][c].ID  # setup parent ID

endID = startID
while (endID == startID):
    endID = random.randint(0,n*n-1)
print("end node ID selected ",endID)

for r in range(2*n-1):
    for c in range(2*n-1):
        if (FullArray[r][c].state == "node" and FullArray[r][c].ID == endID):
            FullArray[r][c].state = "end"
            FullArray[r][c].printable = "x"

#---------------------------------------------------------------------


#---------------------------------------------------------------------
#Print weights
print("\n")
for r in range(2*n-1):
    for c in range(2*n-1):
        print('%02s' % FullArray[r][c].weight, end =" ")
    print("")
print("\n")

#Print all
for r in range(2*n-1):
    for c in range(2*n-1):
        print(FullArray[r][c].printable, end =" ")
    print("")
print("\n")


#---------------------------------------------------------------------
StartTime = timer()
ucs(FullArray,n,startID,10000)
EndTime = timer()
print("Time elapsed for UCS: ", (EndTime-StartTime)*1000," msec\n")
#---------------------------------------------------------------------
FullArray = manhattan(FullArray,NodeArray,n,endID)
StartTime = timer()
astar(FullArray,n,startID,10000)
EndTime = timer()
print("Time elapsed for ASTAR: ", (EndTime-StartTime)*1000," msec\n")
#---------------------------------------------------------------------
StartTime = timer()
ids(FullArray,n,startID,10000)
EndTime = timer()
print("Time elapsed for IDS: ", (EndTime-StartTime)*1000," msec\n")
#--------------------------------------------------------------------