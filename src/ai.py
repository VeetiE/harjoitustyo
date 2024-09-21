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
                score = self.minimax(cur_board_obj, depth - 1, -math.inf, math.inf, False)
                if score > best_score:
                    best_score = score
                    best_col = c
        return best_col


    def heuristic_value(self, board: Board):
        """Gives the board a score that tells the AI how good the current position is for the AI"""
        score = 0
        for r in range(6):
            for c in range(7):
                if board.board[r][c] == 2:
                    score += 1
                elif board.board[r][c] == 1:
                    score-=1
        return score

    def minimax(self,board: Board, depth, alpha, beta,  maximizingPlayer: bool):
        """Goes throught all the possible moves maximizing for the AI and minimizing for the player. Uses alpha beta pruning to cut down the branches"""
        if depth == 0 or board.game_ended:
            return self.heuristic_value(board.board)
        if maximizingPlayer:
            max_evaluation =- math.inf
            for c in range(7):
                if board.board[0][c] == 0:
                    cur_board = board.copy_board()
                    cur_board_obj = Board()
                    cur_board_obj.board = cur_board  
                    cur_board_obj.update_board(cur_board, c, 2)
                    eval = self.minimax(cur_board_obj, depth - 1, alpha, beta, True)
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
                    eval = self.minimax(cur_board_obj, depth - 1, alpha, beta, False)
                    min_evaluation = min(min_evaluation, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
            return min_evaluation   
