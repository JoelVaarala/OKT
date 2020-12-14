from random import randrange, choice

def generateMaze(x,y):

    # list to track which cells has been visited (0= unvisited and 1= visited)
    visitedA = [[0] * x + [1] for _ in range(y)] + [[1] * (x + 1)]
    # Grid for maze 
    horizontal = [["+---"] * x + ["+"] for _ in range(y + 1)]
    vertical = [["|   "] * x + ["|"] for _ in range(y)] + [[]]
    # "Start"
    horizontal[0][0] = "+ S "
    # "Finish"
    horizontal[y][x-1] = "+ E "
    

    # _1 Choose the initial cell, mark it as visited and push it to the stack (numbered comments are pseudocode from wiki)

    # Starting point 
    currentCell = [randrange(x),randrange(y)]
    # stack init
    stack = []
    # add currentCell to stack
    stack.append(currentCell)

    # mark cell as visited 
    visitedA[currentCell[0]][currentCell[1]]= 1
    
    # _2 While the stack is not empty
    
    while stack:

        # 2.1 Pop a cell from the stack and make it a current cell
        currentCell = stack.pop()
        
        # Potential neighboring cells
        pot = [[currentCell[0]+1, currentCell[1]], [currentCell[0],currentCell[1]+1],
		    [currentCell[0]-1, currentCell[1]], [currentCell[0],currentCell[1]-1]]

        # list init 
        neighbors = []

        # checking which of potential neighbors are possible	
        for i in range(len(pot)):
            #if visitedA[pot[i][0]+1][pot[i][1]+1] == 0:
            if visitedA[pot[i][0]][pot[i][1]] == 0:
                if pot[i][0] >= 0 and pot[i][1] >= 0 and pot[i][0] <= x and pot[i][1] <= y:
                    neighbors.append(pot[i])
        
        # 2.2 If the current cell has any neighbours which have not been visited
        if len(neighbors):
            # 2.2.1 Push the current cell to the stack
            stack.append(currentCell)
            # 2.2.2 Choose one of the unvisited neighbours
            nextCell = choice(neighbors)
            # 2.2.3 Remove the wall between the current cell and the chosen cell
            if nextCell[0] == currentCell[0]: 
                horizontal[max(currentCell[1], nextCell[1])][currentCell[0]] = "+   " 
            if nextCell[1] == currentCell[1]: 
                vertical[currentCell[1]][max(currentCell[0], nextCell[0])] = "    "
            # 2.2.4 Mark the chosen cell as visited and push it to the stack
            visitedA[nextCell[0]][nextCell[1]] = 1
            stack.append(nextCell)
    
    
    printableMaze = ""
    for (a, b) in zip(horizontal, vertical):   # zip creates tuples
        printableMaze += ''.join(a + ['\n'] + b + ['\n'])  # /n = new line
    return printableMaze


if __name__ == '__main__':
    #print(generateMaze(10,10))
    print(generateMaze(20,20))
    #print(generateMaze(60,60))

