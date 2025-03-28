import unittest
import blackhole_ai as bh_ai

class TestBlackHoleAI(unittest.TestCase):
    
    def test_evaluating(self):
        test_board = [None, None, (4, "AI"), None, (4, "P1"), None, (2, "AI"), None, (3, "P1"), (3, "AI"), (1, "P1"), None, None, None, (1, "AI"), None, None, (2, "P1"), None, (5, "P1"), None]
        self.assertEqual(bh_ai.evaluate(test_board), 8)

    