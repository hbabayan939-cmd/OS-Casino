import random
from core.config import OS_NAMES, POINTS

class SlotGame:
    def __init__(self, start_points: int = 0, rng: random.Random | None = None):
        self.score = start_points
        self.rng = rng or random.Random()

    def spin(self) -> tuple[list[str], int]:
        reels = [self.rng.choice(OS_NAMES) for _ in range(3)]
        change = self.evaluate(reels)
        self.score += change
        return reels, change

    @staticmethod
    def evaluate(reels: list[str]) -> int:
        if len(set(reels)) == 1:
            return POINTS.get(reels[0], 0)
        return 0