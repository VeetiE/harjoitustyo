class Board:
    def __init__(self):
        self.board=self.new_board()
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
                return (row,col)
        return None
    