import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'src')))

from board import Board

class TestBoard(unittest.TestCase):
    
    def setUp(self):
        """Set up a new board before each test."""
        self.board = Board()

    def test_board_initialization(self):
        """Test if the board is initialized with all zeros."""
        expected_board = [[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0]]
        self.assertEqual(self.board.board, expected_board)

    def test_update_board(self):
        """Test if the board is correctly updated when a chip is added."""
        self.board.update_board(self.board.board, 0, 1)  # Drop chip in column 0
        expected_board = [[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [1, 0, 0, 0, 0, 0, 0]]  # Chip placed in bottom row, first column
        self.assertEqual(self.board.board, expected_board)

    def test_multiple_updates(self):
        """Test if multiple updates in the same column stack correctly."""
        self.board.update_board(self.board.board, 0, 1)
        self.board.update_board(self.board.board, 0, 2)
        expected_board = [[0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0],
                          [2, 0, 0, 0, 0, 0, 0],  # Player 2 on the second row
                          [1, 0, 0, 0, 0, 0, 0]]  # Player 1 on the bottom row
        self.assertEqual(self.board.board, expected_board)

    def test_horizontal_win(self):
        # Create a horizontal line for Player 1 in row 5 (bottom row)
        self.board.update_board(self.board.board,0, 1)
        self.board.update_board(self.board.board,1, 1)
        self.board.update_board(self.board.board,2, 1)
        result = self.board.update_board(self.board.board,3, 1)
        
        # After the 4th chip, Player 1 should win
        self.assertTrue(self.board.check_if_win(result[0], result[1]))
        self.assertTrue(self.board.game_ended)
    
    def test_vertical_win(self):
        # Create a horizontal line for Player 1 in row 5 (bottom row)
        self.board.update_board(self.board.board,0, 1)
        self.board.update_board(self.board.board,1, 1)
        self.board.update_board(self.board.board,2, 1)
        result = self.board.update_board(self.board.board,3, 1)
        
        # After the 4th chip, Player 1 should win
        self.assertTrue(self.board.check_if_win(result[0], result[1]))
        self.assertTrue(self.board.game_ended)
    
    def test_diagonal_win(self):
        # Create a horizontal line for Player 1 in row 5 (bottom row)
        self.board.update_board(self.board.board,0, 1)
        self.board.update_board(self.board.board,1, 1)
        self.board.update_board(self.board.board,2, 1)
        result = self.board.update_board(self.board.board,3, 1)
        
        # After the 4th chip, Player 1 should win
        self.assertTrue(self.board.check_if_win(result[0], result[1]))
        self.assertTrue(self.board.game_ended)
    
    def test_antidiagonal_win(self):
        # Create a horizontal line for Player 1 in row 5 (bottom row)
        self.board.update_board(self.board.board,0, 1)
        self.board.update_board(self.board.board,1, 1)
        self.board.update_board(self.board.board,2, 1)
        result = self.board.update_board(self.board.board,3, 1)
        
        # After the 4th chip, Player 1 should win
        self.assertTrue(self.board.check_if_win(result[0], result[1]))
        self.assertTrue(self.board.game_ended)
if __name__ == "__main__":
    unittest.main()
