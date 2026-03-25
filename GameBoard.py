from GameSquare import GameSquare
import random

class GameBoard:
    def __init__(self,line,column):
        self.rows=line
        self.cols=column
        self.grid_board=[]
        self.total_mines=0
        self.grid_creation()
      
    def grid_creation(self):
        for y in range(self.rows):
            actual_line=[]
            for x in range(self.cols):
                new_case=GameSquare(x,y)
                actual_line.append(new_case)
            self.grid_board.append(actual_line)


    def place_mines(self, first_click_row,first_click_col,mines_total):
        self.total_mines=mines_total
        mine_placed=0
        while mine_placed<mines_total:
            x_aleatory=random.randint(0,self.cols-1)
            y_aleatory=random.randint(0,self.rows-1)

            if x_aleatory==first_click_col and y_aleatory==first_click_row:
                continue

            target_case=self.grid_board[y_aleatory][x_aleatory]

            if not target_case.is_mine:
                target_case.place_mine()
                mine_placed+=1
        self.generate_number()

    def flood_fill(self, x, y):
       
        if x<0 or x>=self.column or y<0 or y>=self.line:
            return
        
        target_case=self.grid_board[y][x]
        if not target_case.is_mine or target_case.is_flag or target_case.is_revealed or target_case.is_point:
            return
        
        target_case.reveal()
        if target_case.mine_around>0:
            return
        
        self.flood_fill(x-1,y)
        self.flood_fill(x+1,y)
        self.flood_fill(x,y-1)
        self.flood_fill(x,y+1)
    
    def generate_number(self):
        for y in range(self.rows):
         for x in range(self.cols):
           actual_case=self.grid_board[y][x]
           if not actual_case.is_mine:
            mines_around=0
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    x_around=x+dx
                    y_around=y+dy
                    if 0<=x_around<self.column and 0<=y_around<self.line:
                        neighbor_case=self.grid_board[y_around][x_around]
                        if neighbor_case.is_mine==True:
                            mines_around+=1
            actual_case.mine_around(mines_around)

    def get_cell(self, row, col):
        return self.grid_board[row][col]
        
    def is_valid(self, row, col):
        return 0<=row<self.rows and 0<=col<self.cols
        
    def mines_left(self):
        flags=sum(1 for row in self.grid_board for case in row if case.is_flag)
        return self.total_mines-flags
                    




