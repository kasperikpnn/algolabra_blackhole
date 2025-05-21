import unittest
import blackhole_ai as blackhole_ai

class TestBlackHoleAI(unittest.TestCase):
    def setUp(self):
        self.bh_ai = blackhole_ai.BlackHoleAI()

    def reset_ai(self):
        self.bh_ai = blackhole_ai.BlackHoleAI()

    def test_valid_move_on_empty_board(self):
        board = [None] * 21
        self.reset_ai()
        move, value = self.bh_ai.process_turn(board, 1, 1)
        self.assertIn(move, range(21))
    
    def test_valid_move_at_very_end(self):
        board = [(1, "P1")] * 19 + [None] * 2
        self.reset_ai()
        move, value = self.bh_ai.process_turn(board, 10, 10)
        self.assertIn(move, [19, 20])

    def test_minimax_loss(self):
        board = [(1, "P1")] * 19 + [None] * 2
        self.reset_ai()
        move, value = self.bh_ai.process_turn(board, 10, 10)
        self.assertEqual(value, -1000)

    def test_minimax_win(self):
        board = [None] + [(5, "P1")] + [(4, "P1")] + [(3, "AI")] + [(3, "P1")] + [(2, "P1")] + [(4, "AI")] + [(2, "AI")] + [(1, "AI")] + [(1, "P1")] + [(5, "AI")] + [(6, "AI")] + [(7, "AI")] + [(7, "P1")] + [(8, "P1")] + [(8, "AI")] + [(9, "P1")] + [(4, "AI")] + [(6, "P1")] + [None] * 2
        self.reset_ai()
        move, value = self.bh_ai.process_turn(board, 10, 10)
        self.assertEqual(value, 1000)
    
    def test_minimax_tie_over_loss(self):
        board = [None] + [(1, "AI")] + [(2, "AI")] + [(5, "AI")] + [(6, "AI")] + [(7, "AI")] + [(8, "AI")] + [(9, "AI")] + [(1, "P1")] + [(2, "P1")] + [(3, "AI")] + [(4, "AI")] + [(5, "P1")] + [(6, "P1")] + [(7, "P1")] + [(3, "P1")] + [None] + [(4, "P1")] + [(8, "P1")] + [(9, "P1")] + [(10, "P1")]
        self.reset_ai()
        move, value = self.bh_ai.process_turn(board, 10, 10)
        self.assertEqual(value, 0)

    def test_minimax_win_over_tie(self):
        board = [None] + [(1, "P1")] + [(2, "P1")] + [(5, "AI")] + [(6, "AI")] + [(7, "AI")] + [(8, "AI")] + [(9, "AI")] + [(1, "AI")] + [(2, "AI")] + [(3, "AI")] + [(4, "AI")] + [(5, "P1")] + [(6, "P1")] + [(7, "P1")] + [(3, "P1")] + [None] + [(4, "P1")] + [(8, "P1")] + [(9, "P1")] + [(10, "P1")]
        self.reset_ai()
        move, value = self.bh_ai.process_turn(board, 10, 10)
        self.assertEqual(value, 1000)