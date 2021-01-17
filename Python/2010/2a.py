#BIO 2010 Q 2a Die Tipping - @starswap
GRID_SIZE = 11 # Constant
class Die():
    def __init__(self):
        self.heading = 0 #0:North,1:East,2:South,3:West
        self.values = [1,6,3,4,5,2] #top,bottom,left,right,front,back
        self.coords = [5,5] #y,x (GLMD) 0,0 is top left, 10,10 is bottom right
    def move(self,direction):
        newValues = list(self.values) # copy it
        if direction == 0:
            self.coords[0] = (self.coords[0] - 1) % GRID_SIZE
            newValues[0] = self.values[4]            #Front to top
            newValues[5] = self.values[0]            #top to back
            newValues[1] = self.values[5]            #back to bottom
            newValues[4] = self.values[1]            #bottom to front
        elif direction == 1:
            self.coords[1] = (self.coords[1] + 1) % GRID_SIZE
            newValues[3] = self.values[0]            #top to right
            newValues[1] = self.values[3]            #right to bottom
            newValues[2] = self.values[1]            #bottom to left
            newValues[0] = self.values[2]            #left to top
        elif direction == 2:
            self.coords[0] = (self.coords[0] + 1) % GRID_SIZE
            newValues[1] = self.values[4]            #front to bottom
            newValues[5] = self.values[1]            #bottom to back
            newValues[0] = self.values[5]            #back to top
            newValues[4] = self.values[0]            #top to front
        elif direction == 3:
            self.coords[1] = (self.coords[1] - 1) % GRID_SIZE
            newValues[2] = self.values[0]            #top to left
            newValues[1] = self.values[2]            #left to bottom
            newValues[3] = self.values[1]            #bottom to right
            newValues[0] = self.values[3]            #right to top
        else:
            print("I am very disappointed")
        self.values = list(newValues)
        self.heading = direction
def printGrid(die,grid):
    neighbours = [-1,0,1]
    for i in neighbours:
        line = ""
        for j in neighbours:
            if die.coords[0]+i >= GRID_SIZE or die.coords[1]+j >= GRID_SIZE or  die.coords[0]+i < 0 or die.coords[1]+j < 0:
                line += "x"
            else:
                line += str(grid[(die.coords[0]+i)][(die.coords[1]+j)])
        print(line)
grid = [[1 for j in range(GRID_SIZE)] for i in range(GRID_SIZE)]
d = Die()
for i in range(3):
    row1 = input()
    splitted = row1.split(" ")
    grid[4+i][4] = int(splitted[0])
    grid[4+i][5] = int(splitted[1])
    grid[4+i][6] = int(splitted[2])
while True:
    moves = int(input())
    if moves == 0:
        break
    else:
        for i in range(moves):
            val = (grid[d.coords[0]][d.coords[1]] + d.values[0])
            if val > 6:
                val -= 6
            grid[d.coords[0]][d.coords[1]] = val
            if val == 1 or val == 6:
                d.move(d.heading)
            elif val == 2:
                d.move((d.heading+1)%4)
            elif val == 3 or val == 4:
                d.move((d.heading+2)%4)
            elif val == 5:
                d.move((d.heading+3)%4)
            else:
                print("I should hope not")
        #print(grid)
        printGrid(d,grid)
                
