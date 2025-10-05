# Globals for the directions
# Change the values as you see fit
EAST = "East"
NORTH = "North"
WEST = "West"
SOUTH = "South"


class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.coordinates = (x_pos, y_pos)
    def move(self,instruction):
        directions = ["North", "East", "South", "West"]
        index = directions.index(self.direction)
        for i in instruction:
            if i == "R":
                if index+1 == len(directions):
                    index = -1
                self.direction = directions[index+1]
                index += 1
            elif i == "L":
                self.direction = directions[index-1]
                index -= 1
            else:
                if self.direction == NORTH:
                    self.coordinates = (self.coordinates[0], self.coordinates[1]+1)
                elif self.direction == SOUTH:
                    self.coordinates = (self.coordinates[0], self.coordinates[1]-1)
                elif self.direction == EAST:
                    self.coordinates = (self.coordinates[0]+1, self.coordinates[1])
                else:
                    self.coordinates = (self.coordinates[0]-1, self.coordinates[1])

        print(self.direction)
        
