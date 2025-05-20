import unittest
import blackhole_ai as blackhole_ai

class TestBlackHoleAI(unittest.TestCase):
    def setUp(self):
        self.bh_ai = blackhole_ai.BlackHoleAI()

    def reset_ai(self):
        self.bh_ai = blackhole_ai.BlackHoleAI()

    def test_create_sum_list(self):
        test_board = [
            None,
            None, (2, "P1"),
            (2, "AI"), (1, "AI"), None,
            (3, "P1"), None, None, None,
            None, (1, "P1"), (3, "AI"), None, (4, "P1"),
            None, None, (5, "AI"), None, (4, "AI"), (5, "P1")
        ]
        test_sums = [2, -1, None, None, None, 1, None, -2, -4, 4, 4, None, None, -3, None, 0, -4, None, -12, None, None]
        self.assertEqual(self.bh_ai.create_sum_list(test_board), test_sums)

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
        board = [(100, "P1")] * 19 + [None] * 2
        self.reset_ai()
        move, value = self.bh_ai.process_turn(board, 10, 10)
        self.assertEqual(value, 1000)
    
    def test_minimax_tie_over_loss(self):
        board =  [None] + [(10, "AI")] * 2 + [(10, "P1")] * 7 + [(10, "AI")] * 2 + [(10, "P1")] * 4 + [None] + [(10, "P1")] * 4
        self.reset_ai()
        move, value = self.bh_ai.process_turn(board, 10, 10)
        self.assertEqual(value, 0)

    def test_minimax_win_over_tie(self):
        board =  [None] + [(10, "P1")] * 2 + [(10, "AI")] * 7 + [(10, "AI")] * 2 + [(10, "AI")] * 4 + [None] + [(10, "P1")] * 4
        self.reset_ai()
        move, value = self.bh_ai.process_turn(board, 10, 10)
        self.assertEqual(value, 1000)