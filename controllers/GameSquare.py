
class GameSquare:
    #Set basic info and default states for the cell
    def __init__(self,x_position,y_position):
        self.x=x_position
        self.y=y_position
        self.is_flag=False
        self.is_mine=False
        self.is_interrogation=False
        self.is_revealed=False
        self.value=0

    #Add or remove flag if cell is hidden
    def change_to_flag(self):

        if not self.is_revealed:
            self.is_flag=not self.is_flag

    #Add or remove question mark if cell is hidden
    def change_to_point(self):

        if not self.is_revealed:
            self.is_interrogation=not self.is_interrogation

    #Show cell if there is no flag
    def reveal(self):

        if not self.is_flag:
         self.is_revealed=True
    
    #Make this cell a mine
    def place_mine(self):

        self.is_mine=True
    
    #Save the number of mines around
    def set_mines(self,number):
            
            self.mine=number