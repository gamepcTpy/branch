import random

class Board:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        row, col = random.choice([(r, c) for r in range(self.size) for c in range(self.size) if self.grid[r][c] == 0])
        self.grid[row][col] = 2 if random.random() < 0.9 else 4

    def can_move(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == 0:
                    return True
                if col < self.size - 1 and self.grid[row][col] == self.grid[row][col + 1]:
                    return True
                if row < self.size - 1 and self.grid[row][col] == self.grid[row + 1][col]:
                    return True
        return False
