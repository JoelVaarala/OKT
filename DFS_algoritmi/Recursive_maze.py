from random import shuffle, randrange
import sys
 
def generateMaze(x, y):
    
    # list to track which cells has been visited
    visited = [[0] * x + [1] for _ in range(y)] + [[1] * (x + 1)]
    # Grid
    vertical = [["|   "] * x + ["|"] for _ in range(y)] + [[]]  
    horizontal = [["+---"] * x + ["+"] for _ in range(y + 1)]      
    
    # "Start" and "End" points
    horizontal[0][0] = "+ S "
    horizontal[y][x-1] = "+ E " #vertical[x-1][y]

    # this shows the recursion limit you have
    print(sys.getrecursionlimit())

    def removeWalls(x, y):
        visited[y][x] = 1
 
        neighbors = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)] # cells around the currentCell
        shuffle(neighbors) # shuffles the values so the order is randomized
       
        for (nx, ny) in neighbors: # loop trough neighboring cells

            if visited[ny][nx]: 
                continue  # incase cell has been visited already skip to the next neihgbor
            if nx == x: 
                horizontal[max(y, ny)][x] = "+   " # max() returns highest of the values
            if ny == y: 
                vertical[y][max(x, nx)] = "    "

            removeWalls(nx, ny) # recursive call, so the function calls itself with new cell "coordinates" parameters
 
    
    # Starting point as param, could be any cell
    removeWalls(randrange(x), randrange(y))

    # After the function has completed, return maze 
    printableMaze = ""
    for (a, b) in zip(horizontal, vertical):   # zip creates tuples from lists inside of hor & ver
        printableMaze += ''.join(a + ['\n'] + b + ['\n'])  # /n = line change for each list
        #print(s)
    return printableMaze
 
if __name__ == '__main__':
    print(generateMaze(10, 10))
    #print(generateMaze(5, 5))
    #print(generateMaze(60,60))