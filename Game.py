from GameBoard import GameBoard

class Game:
    def __init__(self,rows,column,window):
        self.rows=rows
        self.column=column
        self.window=window
        self.board=GameBoard(rows,column)

    def check_victory(self):
        hidden_cases=0
        for y in range(self.board.rows):
            for x in range(self.board.cols):
                if not self.board.grid_board[x][y].is_revealed:
                    hidden_cases+=1
        if hidden_cases==self.board.total_mines:
         self.window.on_game_over(True)
            
    def reveal(self,row,col):
        target_case=self.board.get_cell(row,col)
        if target_case.is_mine:
            target_case.reveal()
            self.window.on_game_over(False)
            return
        self.board.flood_fill(col,row)
        self.check_victory()
    
    def cycle_flag(self,row,col):

        target_case=self.board.get_cell(row,col)
        target_case.change_to_flag()
       



