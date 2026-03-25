from GameBoard import GameBoard

class Game:
    def __init__(self,rows,column,window):
        #Initialize the game controller
        self.rows=rows
        self.column=column
        self.window=window
        self.board=GameBoard(rows,column)

    def check_victory(self):
        #Initialize counter for hidden cases
        hidden_cases=0
        #Search in rows and columns of board
        for y in range(self.board.rows):
            for x in range(self.board.cols):
                #Check if current cell is still hidden
                if not self.board.grid_board[y][x].is_revealed:
                    #Increment the hidden cells counter
                    hidden_cases+=1
        #Check if the remaining hidden cells match the total mines
        if hidden_cases==self.board.total_mines:
         #If yes, change to a win state
         self.window.on_game_over(True)
            
    def reveal(self,row,col):
        #Take the specific cell clicked by the user
        target_case=self.board.get_cell(row,col)
        #Check if the clicked cell contains a mine
        if target_case.is_mine:
            #Reveal the mine
            target_case.reveal()
            #If it's a mine, game over
            self.window.on_game_over(False)
        
            return
        #If safe, trigger the recursive reveal algorithm, if yes it's victory
        self.board.flood_fill(col,row)
        self.check_victory()
    
    def cycle_flag(self,row,col):

        #Take the cell clicked by the user
        target_case=self.board.get_cell(row,col)
        #Place the flag state on this cell
        target_case.change_to_flag()
