import numpy as np
import random


class TaxiEnv:
    def __init__(self):
        self.size = 10
        self.walls = [
            (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
            (5, 3), (5, 4), (5, 5), (5, 6), (5, 7),
            (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6),
            (3, 8), (4, 8), (5, 8), (6, 8), (1, 5), (8, 5)
        ]
        self.locations = {
            'A': (0, 0),
            'B': (0, 9),
            'C': (9, 0),
            'D': (9, 9)
        }
        self.actions = [0, 1, 2, 3, 4, 5]  # Down, Up, Right, Left, Pickup, Dropoff
        self.reset()

    @property
    def pickup(self):
        return self._pickup

    @pickup.setter
    def pickup(self, value):
        if isinstance(value, str):
            self._pickup = self.locations[value]
        else:
            self._pickup = value

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        if isinstance(value, str):
            self._destination = self.locations[value]
        else:
            self._destination = value

    def reset(self, pickup=None, destination=None):
        # Set pickup and destination
        if pickup and destination:
            self.pickup = pickup
            self.destination = destination
        else:
            locs = list(self.locations.keys())
            while True:
                p, d = random.sample(locs, 2)
                if p != d:
                    self.pickup = p
                    self.destination = d
                    break

        # Initialize taxi position (not at pickup/destination)
        while True:
            self.taxi_pos = (random.randint(0, self.size - 1),
                             random.randint(0, self.size - 1))
            if (self.taxi_pos != self.pickup and
                    self.taxi_pos != self.destination):
                break

        self.has_passenger = False
        return self._get_state()

    def _get_state(self):
        return (*self.taxi_pos,
                *self.pickup,
                *self.destination,
                self.has_passenger)

    def _is_valid(self, pos):
        x, y = pos
        return (0 <= x < self.size and
                0 <= y < self.size and
                pos not in self.walls)

    def step(self, action):
        reward = -1  # Time penalty
        done = False
        x, y = self.taxi_pos

        # Movement actions
        if action == 0:
            new_pos = (x + 1, y)  # Down
        elif action == 1:
            new_pos = (x - 1, y)  # Up
        elif action == 2:
            new_pos = (x, y + 1)  # Right
        elif action == 3:
            new_pos = (x, y - 1)  # Left
        else:
            new_pos = (x, y)

        if action <= 3:
            if self._is_valid(new_pos):
                self.taxi_pos = new_pos
            else:
                reward -= 2  # Extra penalty for hitting wall

        # Pickup action
        elif action == 4:
            if self.taxi_pos == self.pickup and not self.has_passenger:
                self.has_passenger = True
                reward = 10
            else:
                reward = -10

        # Dropoff action
        elif action == 5:
            if self.taxi_pos == self.destination and self.has_passenger:
                done = True
                reward = 20
            else:
                reward = -10

        return self._get_state(), reward, done

    def render(self):
        grid = np.full((self.size, self.size), '.', dtype='object')

        # Add walls
        for wall in self.walls:
            grid[wall] = '#'

        # Add locations
        grid[self.pickup] = 'P'
        grid[self.destination] = 'D'

        # Add taxi
        tx, ty = self.taxi_pos
        grid[tx, ty] = 'T' if not self.has_passenger else 'Ṫ'

        # Print grid
        print("+" + "---+" * self.size)
        for row in grid:
            print("| " + " | ".join(row) + " |")
            print("+" + "---+" * self.size)
        print(f"Passenger: {'In taxi' if self.has_passenger else 'At pickup'}")
        print(f"Destination: {self.destination}\n")