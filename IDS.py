# Setup (Match cords to start)
# LOOP:
# New Max depth --> Flush arrays, re-append start node to closelist
# DEPTH-LOOP:
#   Check to increase depth if openlist is empty
#   Set current Cords to last explored Node
#   Calculate Total weight
#   Add to closelist
#   Remove from openlist
#   Add valid neighbours to openlist
#   Check if max nodes reached --> Failure
#   Check if goal is reached

def ids (FullArray,n,startID,max):
    openlist = []
    closelist = []
    totalweight=0
    finish = False
    maxdepth = 0
    totalNodes = 0

    #detect start id cords in Fullarray
    for r in range(2 * n - 1):
        for c in range(2 * n - 1):
            if (FullArray[r][c].state == "start" and FullArray[r][c].ID == startID):
                startR = r
                startC = c
    #print("start node id ",startID," ",currentC," ",currentR)


    while (not finish):
        #New depth -> Flush arrays, re-append start node to closelist
        maxdepth += 1
        currentR = startR
        currentC = startC
        totalNodes += len(closelist)
        openlist.clear()
        closelist.clear()
        openlist.append(FullArray[currentR][currentC])
        increasedepth = False

        while (not increasedepth):

            if (not openlist):
                #Depth increase when openlist is empty
                #print("Increasing depth to", maxdepth + 1)
                increasedepth = True
                break

            #temp2 = openlist[len(openlist)-1]
            #print("Node2 ID:", temp2.ID, "Parent:", temp2.parentID, "depth:", temp2.depth, "weight:", temp2.combinedweight)

            currentR = openlist[len(openlist)-1].r
            currentC = openlist[len(openlist)-1].c
            totalweight = openlist[len(openlist)-1].combinedweight
            closelist.append(openlist[len(openlist)-1])

            openlist.pop()

            #checkup
            if (currentR != 0 and  FullArray[currentR-1][currentC].Deleted == False and unvisited(FullArray[currentR-2][currentC],closelist,openlist) and (FullArray[currentR][currentC].depth + 1 <= maxdepth)):
                temp = FullArray[currentR-2][currentC]
                temp.combinedweight = totalweight + FullArray[currentR-1][currentC].weight #adds weight of link
                temp.parentID = FullArray[currentR][currentC].ID                                  #setup parent ID
                temp.depth = FullArray[currentR][currentC].depth + 1                              #setup depth in node addition
                FullArray[currentR-2][currentC].depth = (FullArray[currentR][currentC].depth + 1) #setup depth on the board
                openlist.append(temp)
            #checkright
            if (currentC != 2 * n - 2 and  FullArray[currentR][currentC+1].Deleted == False and unvisited(FullArray[currentR][currentC+2],closelist,openlist) and (FullArray[currentR][currentC].depth + 1 <= maxdepth)):
                temp = FullArray[currentR][currentC+2]
                temp.combinedweight = totalweight + FullArray[currentR][currentC+1].weight
                temp.parentID = FullArray[currentR][currentC].ID                                  #setup parent ID
                temp.depth = FullArray[currentR][currentC].depth + 1                              #setup depth in node addition
                FullArray[currentR][currentC+2].depth = (FullArray[currentR][currentC].depth + 1) #setup depth on the board
                openlist.append(temp)
            #checkdown
            if (currentR != 2 * n - 2 and  FullArray[currentR+1][currentC].Deleted == False and unvisited(FullArray[currentR+2][currentC],closelist,openlist) and (FullArray[currentR][currentC].depth + 1 <= maxdepth)):
                temp = FullArray[currentR+2][currentC]
                temp.combinedweight = totalweight + FullArray[currentR+1][currentC].weight #adds weight of link
                temp.parentID = FullArray[currentR][currentC].ID                                  #setup parent ID
                temp.depth = FullArray[currentR][currentC].depth + 1                              #setup depth in node addition
                FullArray[currentR+2][currentC].depth = (FullArray[currentR][currentC].depth + 1) #setup depth on the board
                openlist.append(temp)
            #checkleft
            if (currentC != 0 and  FullArray[currentR][currentC-1].Deleted == False and unvisited(FullArray[currentR][currentC-2],closelist,openlist)and (FullArray[currentR][currentC].depth + 1 <= maxdepth)):
                temp = FullArray[currentR][currentC-2]
                temp.combinedweight = totalweight + FullArray[currentR][currentC-1].weight
                temp.parentID = FullArray[currentR][currentC].ID                                  #setup parent ID
                temp.depth = FullArray[currentR][currentC].depth + 1                             #setup depth in node addition
                FullArray[currentR][currentC-2].depth = (FullArray[currentR][currentC].depth + 1) #setup depth on the board
                openlist.append(temp)

            #check for max nodes visited / can be altered to trigger with max depth reached
            if (totalNodes > max):
                print("process failed, end goal is not accessible :c\nMaximum depth:",maxdepth)
                finish = True
                break

            #print("Current: ",nextnode.ID,"Parent: ",nextnode.parentID,"depth: ",nextnode.depth,"weight: ",nextnode.combinedweight)

            #Goal reached/ finds path in close list
            if (closelist[len(closelist)-1].state == "end"):
                finish = True
                temp = closelist[len(closelist)-1]
                print("Goal achieved, number of nodes visited:", totalNodes-1,"(plus the start node) Maximum depth:",maxdepth,"\nCorrect path: (end...start)" )
                print("Node ID:", temp.ID, "Parent:", temp.parentID, "depth:", temp.depth, "weight:",temp.combinedweight)
                for x in range(temp.depth):
                    for i in range(len(closelist)):
                        if (closelist[i].ID == temp.parentID):
                            temp = closelist[i]
                            print("Node ID:", temp.ID, "Parent:", temp.parentID, "depth:", temp.depth, "weight:",temp.combinedweight)




def unvisited (node,closelist,openlist):
    check=True
    for i in range(len(closelist)):
        if (node.ID == closelist[i].ID):
            check=False
    for i in range(len(openlist)):
        if (node.ID == openlist[i].ID):
            check=False
    return check