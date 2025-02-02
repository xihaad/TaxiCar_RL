import numpy as np


class TaxiEnv:
    def __init__(self, size=5):
        self.size = size
        self.walls = [(1, 1), (1, 3), (3, 1), (3, 3)]
        self.passenger_pos = (0, 0)
        self.destination = (4, 4)
        self.taxi_pos = (2, 2)
        self.has_passenger = False
        self.actions = ["up", "down", "left", "right", "pickup", "dropoff"]

    def reset(self):
        self.taxi_pos = (2, 2)
        self.has_passenger = False
        return self._get_state()

    def _get_state(self):
        return (*self.taxi_pos, self.has_passenger, *self.destination)

    def _is_valid_move(self, pos):
        x, y = pos
        return 0 <= x < self.size and 0 <= y < self.size and pos not in self.walls

    def step(self, action):
        reward = -1  # Default step penalty
        done = False
        x, y = self.taxi_pos

        if action == "up":
            new_pos = (x - 1, y)
        elif action == "down":
            new_pos = (x + 1, y)
        elif action == "left":
            new_pos = (x, y - 1)
        elif action == "right":
            new_pos = (x, y + 1)
        else:
            new_pos = (x, y)

        if action in ["up", "down", "left", "right"]:
            if self._is_valid_move(new_pos):
                self.taxi_pos = new_pos
            else:
                reward = -3  # Wall collision penalty

        elif action == "pickup":
            if self.taxi_pos == self.passenger_pos and not self.has_passenger:
                self.has_passenger = True
                reward = 10
            else:
                reward = -10

        elif action == "dropoff":
            if self.taxi_pos == self.destination and self.has_passenger:
                done = True
                reward = 20
            else:
                reward = -10

        return self._get_state(), reward, done

    def render(self):
        grid = np.full((self.size, self.size), '.')
        for wall in self.walls:
            grid[wall] = '#'
        grid[self.passenger_pos] = 'P'
        grid[self.destination] = 'D'
        x, y = self.taxi_pos
        grid[x, y] = 'T' if not self.has_passenger else 'Ṫ'

        print("+" + "---+" * self.size)
        for row in grid:
            print("| " + " | ".join(row) + " |")
            print("+" + "---+" * self.size)
        print(f"Passenger: {'With taxi' if self.has_passenger else 'At P'}")
        print(f"Destination: D")