from controllers.GameBoard import GameBoard

class Game:
    #Create the game and the board
    def __init__(self,rows,cols,window):
        self.rows=rows
        self.cols=cols
        self.window=window
        self.board=GameBoard(rows,cols)

    #Check if the player won the game
    def check_victory(self):
        
        hidden_cases=0
        for y in range(self.board.rows):
            for x in range(self.board.cols):
                if not self.board.grid_board[y][x].is_revealed:
                    hidden_cases+=1
        if hidden_cases==self.board.total_mines:
         self.window.on_game_over(True)
            
    #Play a turn when clicking left
    def reveal(self,row,col):

        target_case=self.board.get_cell(row,col)
        if target_case.is_mine:
            target_case.reveal()
            self.window.on_game_over(False)
            return
        self.board.flood_fill(col,row)
        self.check_victory()
    
    #Put or remove a flag when clicking right
    def cycle_flag(self,row,col):

        target_case=self.board.get_cell(row,col)
        target_case.change_to_flag()