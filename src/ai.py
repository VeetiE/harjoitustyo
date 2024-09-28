import math
from board import Board

class AI:
    def __init__(self):
        pass
    
    def find_best_move(self, board: Board, depth):
        """Finds the best move for AI"""
        best_score=-math.inf
        best_col=None
        for c in range(7):
            if board.board[0][c] == 0:
                cur_board = board.copy_board()
                cur_board_obj = Board()  
                cur_board_obj.board = cur_board  
                cur_board_obj.update_board(cur_board, c, 2)
                score = self.minimax(cur_board_obj, depth - 1, -math.inf, math.inf, True)

                if score > best_score:
                    best_score = score
                    best_col = c
        return best_col
    def score_line(self, line):
        score=0
        if line.count(2)==4:
            return math.inf
        if line.count(2)==3:
            score+=100
        if line.count(2)==2:
            score+=10
        if line.count(1)==4:
            return -math.inf
        if line.count(1)==3:
            score-=100
        if line.count(1)==2:
            score-=10
        return score

    def heuristic_value(self, board: Board):
        """Gives the board a score that tells the AI how good the current position is for the AI"""
        score=0
        """check horizontal"""
        for r in range(6):
            for c in range(4):
                line=[board.board[r][c+i] for i in range(4)]
                score+=self.score_line(line)
        """check vertical"""
        for c in range(7):
            for r in range(3):
                line=[board.board[r+i][c] for i in range(4)]
                score+=self.score_line(line)
        """check diagonal"""
        for r in range(3):
            for c in range(4):
                line=[board.board[r+i][c+i] for i in range(4)]
                score+=self.score_line(line)
        """check antidiagonal"""
        for r in range(3,6):
            for c in range(4):
                line=[board.board[r-i][c+i] for i in range(4)]
                score+=self.score_line(line)
        return score
    
    def minimax(self,board: Board, depth, alpha, beta,  maximizingPlayer: bool):
        """Goes throught all the possible moves maximizing for the AI and minimizing for the player. Uses alpha beta pruning to cut down the branches"""
        if depth == 0 or board.game_ended:
            return self.heuristic_value(board)
        if all(board.board[0][col] != 0 for col in range(7)):
            return 0
        if maximizingPlayer:
            max_evaluation =- math.inf
            for c in range(7):
                if board.board[0][c] == 0:
                    cur_board = board.copy_board()
                    cur_board_obj = Board()
                    cur_board_obj.board = cur_board  
                    cur_board_obj.update_board(cur_board, c, 2)
                    eval = self.minimax(cur_board_obj, depth - 1, alpha, beta, False)
                    max_evaluation = max(max_evaluation, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
            return max_evaluation
        else:
            min_evaluation = math.inf
            for c in range(7):
                
                if board.board[0][c] == 0:
                    cur_board = board.copy_board()
                    cur_board_obj = Board()  
                    cur_board_obj.board = cur_board  
                    cur_board_obj.update_board(cur_board, c, 1)
                    eval = self.minimax(cur_board_obj, depth - 1, alpha, beta, True)
                    min_evaluation = min(min_evaluation, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_evaluation   
