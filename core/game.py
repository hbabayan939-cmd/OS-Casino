import random
from core.config import OS_NAMES, POINTS

class SlotGame:
    def __init__(self, start_points: int = 0, rng: random.Random | None = None):
        self.score = start_points
        self.rng = rng or random.Random()

    def spin(self) -> tuple[str, int]:
        result = self.rng.choice(OS_NAMES)
        change = POINTS[result]
        self.score += change
        return result, change
