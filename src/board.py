import copy
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
    def copy_board(self):
        return copy.deepcopy(self.board)
    def update_board(self,board, col, chip):
        for row in range(5, -1, -1):
            if board[row][col]==0:
                board[row][col]=chip
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
            for c in range(max(0, col - 3), min(6, col + 3) + 1):
                if self.board[row][c]==chip:
                    counter+=1
                    if counter==4:
                        return True
                else:
                    counter=0
            return False
        def check_vertical():
            counter=0
            for r in range(max(0, row-3), min(5, row+3)+1):
                if self.board[r][col]==chip:
                    counter+=1
                    if counter==4:
                        return True
                else:
                    counter=0
        def check_diagonal():
            counter=0
            r=row
            c=col

            while min(r,c)>0:
                r-=1
                c-=1
            while r<=5 and c<=6:
                if self.board[r][c]==chip:
                    counter+=1
                    if counter==4:
                        return True
                else:
                    counter=0
                r+=1
                c+=1
            return False
        def check_antidiagonal():
            counter=0
            r=row
            c=col

            while r>0 and c<6:
                r-=1
                c+=1
            while r<=5 and c>=0:
                if self.board[r][c]==chip:
                    counter+=1
                    if counter==4:
                        return True
                else:
                    counter=0
                r+=1
                c-=1
            return False

            

        return check_horizontal() or check_vertical() or check_diagonal() or check_antidiagonal()

    