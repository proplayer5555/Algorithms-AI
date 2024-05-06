# Setup (Match cords to start)
# LOOP:
# Add valid neighbours to openlist
# Check if openlist is empty/ max nodesm reached --> Failure
# Choose node with min weight from openlist
# Remove from openlist
# Add to closelist
# Calculate Total weight
# Set current Cords to next node
# Check if goal is reached
#

def ucs (FullArray,n,startID,max):
    openlist = []
    closelist = []
    totalweight=0
    currentR = 0
    currentC = 0
    finish = False

    #detect start id cords in Fullarray
    for r in range(2 * n - 1):
        for c in range(2 * n - 1):
            if (FullArray[r][c].state == "start" and FullArray[r][c].ID == startID):
                currentR = r
                currentC = c
    closelist.append(FullArray[currentR][currentC])
    #print("start node id ",startID," ",currentC," ",currentR)

    while (not finish):
        #checkup
        if (currentR != 0 and  FullArray[currentR-1][currentC].Deleted == False and unvisited(FullArray[currentR-2][currentC],closelist,openlist)):
            temp = FullArray[currentR-2][currentC]
            temp.combinedweight = totalweight + FullArray[currentR-1][currentC].weight #adds weight of link
            temp.parentID = FullArray[currentR][currentC].ID                                  #setup parent ID
            temp.depth = FullArray[currentR][currentC].depth + 1                              #setup depth in node addition
            FullArray[currentR-2][currentC].depth = (FullArray[currentR][currentC].depth + 1) #setup depth on the board
            openlist.append(temp)
        #checkright
        if (currentC != 2 * n - 2 and  FullArray[currentR][currentC+1].Deleted == False and unvisited(FullArray[currentR][currentC+2],closelist,openlist)):
            temp = FullArray[currentR][currentC+2]
            temp.combinedweight = totalweight + FullArray[currentR][currentC+1].weight
            temp.parentID = FullArray[currentR][currentC].ID                                  #setup parent ID
            temp.depth = FullArray[currentR][currentC].depth + 1                              #setup depth in node addition
            FullArray[currentR][currentC+2].depth = (FullArray[currentR][currentC].depth + 1) #setup depth on the board
            openlist.append(temp)
        #checkdown
        if (currentR != 2 * n - 2 and  FullArray[currentR+1][currentC].Deleted == False and unvisited(FullArray[currentR+2][currentC],closelist,openlist)):
            temp = FullArray[currentR+2][currentC]
            temp.combinedweight = totalweight + FullArray[currentR+1][currentC].weight #adds weight of link
            temp.parentID = FullArray[currentR][currentC].ID                                  #setup parent ID
            temp.depth = FullArray[currentR][currentC].depth + 1                              #setup depth in node addition
            FullArray[currentR+2][currentC].depth = (FullArray[currentR][currentC].depth + 1) #setup depth on the board
            openlist.append(temp)
        #checkleft
        if (currentC != 0 and  FullArray[currentR][currentC-1].Deleted == False and unvisited(FullArray[currentR][currentC-2],closelist,openlist)):
            temp = FullArray[currentR][currentC-2]
            temp.combinedweight = totalweight + FullArray[currentR][currentC-1].weight
            temp.parentID = FullArray[currentR][currentC].ID                                  #setup parent ID
            temp.depth = FullArray[currentR][currentC].depth + 1                             #setup depth in node addition
            FullArray[currentR][currentC-2].depth = (FullArray[currentR][currentC].depth + 1) #setup depth on the board
            openlist.append(temp)

        if (not openlist or len(closelist) > max):
            print("process failed, end goal is not accessible :c")
            finish = True
            break

        #decide
        nextnode=openlist[0]
        for i in range(len(openlist)):
            temp=openlist[i-1]
            if (temp.combinedweight < nextnode.combinedweight):
                nextnode=temp

        # remove from openlist
        for i in range(len(openlist)):
            if (openlist[i-1].ID == nextnode.ID):
                openlist.pop(i-1)

        closelist.append(nextnode)
        totalweight = nextnode.combinedweight
        #print("Current: ",nextnode.ID,"Parent: ",nextnode.parentID,"depth: ",nextnode.depth,"weight: ",nextnode.combinedweight)
        currentR=nextnode.r
        currentC=nextnode.c

        # Goal reached/ finds path in close list
        if (nextnode.state == "end"):
            finish = True
            print("Goal achieved, number of nodes visited:", len(closelist)-1,"(plus the start node)\nCorrect path: (end...start)" )
            print("Node ID:", nextnode.ID, "Parent:", nextnode.parentID, "depth:", nextnode.depth, "weight:",nextnode.combinedweight)
            for x in range(nextnode.depth):
                for i in range(len(closelist)):
                    if (closelist[i].ID == nextnode.parentID):
                        nextnode = closelist[i]
                        print("Node ID:", nextnode.ID, "Parent:", nextnode.parentID, "depth:", nextnode.depth, "weight:",nextnode.combinedweight)





def unvisited (node,closelist,openlist):
    check=True
    for i in range(len(closelist)):
        if (node.ID == closelist[i].ID):
            check=False
    for i in range(len(openlist)):
        if (node.ID == openlist[i].ID):
            check=False
    return check