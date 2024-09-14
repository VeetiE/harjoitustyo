class Board:
    def __init__(self):
        self.board=self.new_board()
        self.game_ended=False
    def new_board(self):
        board=[[0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],
               [0,0,0,0,0,0,0],]
        return  board
    def update_board(self, col, chip):
        for row in range(5, -1, -1):
            if self.board[row][col]==0:
                self.board[row][col]=chip
                if self.check_if_win(row, col)==True:
                    self.game_ended=True
                return (row,col)
        return None
    
    def check_if_win(self, row, col):
        chip=self.board[row][col]
        if chip==0:
            return False
        def check_horizontal():
            counter=0
            for c in range(max(0, col-3), min(6, col+3)+1):
                if self.board[row][c]==chip:
                    counter+=1
                    if counter==4:
                        return True
                else:
                    counter=0
            return False
        return check_horizontal()

    