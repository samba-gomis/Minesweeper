from GameSquare import GameSquare
import random

class GameBoard:
    def __init__(self,line,column):
        self.line=line
        self.column=column
        self.grid_board=[]
      
    def grid_creation(self):
        for y in range(self.line):
            actual_line=[]
            for x in range(self.column):
                new_case=GameSquare(x,y)
        actual_line.append(new_case)
        self.grid_board.append(actual_line)
        print(self.grid_board)        

    def flood_fill(self, x, y):
        if self.squares.is_mine or self.squares.is_flag:
            return
        self.flood_fill(x-1,y)
        self.flood_fill(x+1,y)
        self.flood_fill(x,y-1)
        self.flood_fill(x,y+1)

