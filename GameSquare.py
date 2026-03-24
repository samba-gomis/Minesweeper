
class GameSquare:
    def __init__(self,x_position, y_position):
        self.x=x_position
        self.y=y_position
        self.is_flag=False
        self.is_mine=False
        self.is_revealed=False
        self.mine_around=0

    def change_to_flag(self):
        if not self.is_revealed:
            self.is_flag=not self.is_flag
    
    def reveal(self):
        if not self.is_flag:
         self.is_revealed=True
    
    def place_mine(self):
        self.is_mine=True
    
    def set_mines(self, number):
            self.mine=number



    