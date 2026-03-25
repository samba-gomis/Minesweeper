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

    def generate_mines(self, mines_total):
        mine_placed=0
        while mine_placed<mines_total:
            x_aleatory=random.randint(0,self.column-1)
            y_aleatory=random.randint(0,self.line-1)
            target_case=self.grid_board[y_aleatory, x_aleatory]
            if target_case.is_mine:
                target_case.place_mine()
                mine_placed+=1

    def flood_fill(self, x, y):
       
        if x<0 or x>=self.column or y<0 or y>=self.line:
            return
        
        target_case=self.grid_board[y,x]
        if target_case.is_mine or target_case.is_flag or target_case.is_revealed or target_case.is_point:
            return
        
        target_case.reveal()
        if target_case.mine_around>0:
            return
        
        self.flood_fill(x-1,y)
        self.flood_fill(x+1,y)
        self.flood_fill(x,y-1)
        self.flood_fill(x,y+1)

