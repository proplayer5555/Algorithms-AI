def manhattan (FullArray,NodeArray,n,endID):
    endR = 0
    endC = 0
    finish = False
    #Find end Node cords in Node array
    for r in range(n):
        for c in range(n):
            if (NodeArray[r][c].ID == endID):
                endR = r
                endC = c

    #Calculate manhattan distance for each Node in NodeArray
    for r in range(n):
        for c in range(n):
            NodeArray[r][c].manhattan = 1*(abs(r-endR)+abs(c-endC)) #Can modify manhattan strength
    """
    # Print all
    for r in range(n):
        for c in range(n):
            print(NodeArray[r][c].manhattan, end=" ")
        print("")
    print("\n")
    """

    #Match NodeArray with FullArray
    for r in range(n):
        for c in range(n):
            for r1 in range(2 * n - 1):
                for c1 in range(2 * n - 1):
                    if ((FullArray[r1][c1].state == "start" or FullArray[r1][c1].state == "node") and FullArray[r1][c1].ID == NodeArray[r][c].ID):
                        FullArray[r1][c1].manhattan = NodeArray[r][c].manhattan

    #return FullArray
    return FullArray