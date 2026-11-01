import random
import unittest
from core.config import POINTS
from core.game import SlotGame


class TestSlotGame(unittest.TestCase):
    def test_three_linux_gives_highest_points(self):
        self.assertEqual(SlotGame.evaluate(["Linux"] * 3), POINTS["Linux"])
        self.assertEqual(max(POINTS.values()), POINTS["Linux"])

    def test_mixed_reels_give_nothing(self):
        self.assertEqual(SlotGame.evaluate(["Linux", "Windows", "Linux"]), 0)

    def test_windows_and_macos_reduce_points(self):
        self.assertLess(SlotGame.evaluate(["Windows"] * 3), 0)
        self.assertLess(SlotGame.evaluate(["macOS"] * 3), 0)

    def test_spin_updates_score(self):
        game = SlotGame(start_points=10, rng=random.Random(1))
        reels, change = game.spin()
        self.assertEqual(len(reels), 3)
        self.assertEqual(game.score, 10 + change)


if __name__ == "__main__":
    unittest.main()