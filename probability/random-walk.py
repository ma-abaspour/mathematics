
import random
from collections import defaultdict

class RandomWalk:
    def __init__(self, dimensions=1, rules=None, start=None):
        self.dimensions = dimensions
        self.position = start or (0,) * dimensions
        self.rules = rules or self.default_rules
        self.path = [self.position]
        self.visits = defaultdict(int)
        self.visits[self.position] += 1

    def default_rules(self):
      # Default rules: equal probability to move ±1 in each dimension
      moves = []
      for d in range(self.dimensions):
          move_positive = tuple(1 if i == d else 0 for i in range(self.dimensions))
          move_negative = tuple(-1 if i == d else 0 for i in range(self.dimensions))
          moves.extend([move_positive, move_negative])
      return moves

    def step(self):
        move = random.choice(self.rules())
        self.position = tuple(p + m for p, m in zip(self.position, move))
        self.path.append(self.position)
        self.visits[self.position] += 1

    def simulate(self, steps):
        for _ in range(steps):
            self.step()
        return self.path


def probability_return_to_origin(walk):
    return walk.path[-1] == (0,) * walk.dimensions

def first_passage_time(walk, target):
    for t, position in enumerate(walk.path):
        if position == target:
            return t
    return float('inf')  # Never reached

def expected_distance(walk):
    return sum(sum(abs(x) for x in position) for position in walk.path) / len(walk.path)

def simulate_and_analyze(walk_class, steps, trials, analysis_fn, **kwargs):
    results = []
    for _ in range(trials):
        walk = walk_class(**kwargs)
        walk.simulate(steps)
        results.append(analysis_fn(walk))
    return sum(results) / trials  # Mean of all trials


rw_1d = lambda: RandomWalk(dimensions=1)
print("P(Return to origin after 10 steps):", 
      simulate_and_analyze(rw_1d, steps=10, trials=10000, analysis_fn=probability_return_to_origin))


rw_2d = lambda: RandomWalk(dimensions=2)
target = (2, 2)
print("Expected First Passage Time to (2, 2):",
      simulate_and_analyze(rw_2d, steps=50, trials=10000, analysis_fn=lambda walk: first_passage_time(walk, target)))


print("Expected Distance from Origin (10 steps, 2D):",
      simulate_and_analyze(rw_2d, steps=10, trials=10000, analysis_fn=expected_distance))


