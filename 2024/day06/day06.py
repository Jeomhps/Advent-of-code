"""
Author: Jeomhps
Date  : 2024-12-06
AoC 2024 Day 6 - https://adventofcode.com/2024/day/6
"""

from sys import argv

class Map:
    def __init__(self, file_path):
        self.grid = self.load_map(file_path)
        self.rows = len(self.grid)
        self.cols = len(self.grid[0])
        self.player_pos = self.find_guard()
        self.visited_positions = set()
        self.visited_count = 0
        self.directions = ['up', 'right', 'down', 'left']
        self.current_direction = 'up'

    def load_map(self, file_path):
        with open(file_path, 'r') as file:
            return [list(line.strip()) for line in file.readlines()]

    def find_guard(self):
        for i, row in enumerate(self.grid):
            for j, cell in enumerate(row):
                if cell == '^':
                    return (i, j)
        raise ValueError("(^) not found in the map")

    def move_guard(self):
        moves = {
            'up': (-1, 0),
            'right': (0, 1),
            'down': (1, 0),
            'left': (0, -1),
        }

        while True:
            dx, dy = moves[self.current_direction]
            x, y = self.player_pos
            new_x, new_y = x + dx, y + dy

            if (
                0 <= new_x < self.rows and 0 <= new_y < self.cols
                and self.grid[new_x][new_y] != '#'
            ):
                if (new_x, new_y) not in self.visited_positions:
                    self.visited_positions.add((new_x, new_y))
                    self.visited_count += 1
                self.grid[x][y] = 'X'

                self.grid[new_x][new_y] = '^'
                self.player_pos = (new_x, new_y)
            else:
                current_index = self.directions.index(self.current_direction)
                self.current_direction = self.directions[(current_index + 1) % 4]

            if not (0 <= new_x < self.rows and 0 <= new_y < self.cols):
                self.grid[x][y] = 'X'
                break

    def display(self):
        for row in self.grid:
            print("".join(row))
        print(f"Visited cells: {self.visited_count}")

def p1(filename):
    map = Map(filename)
    map.move_guard()
    map.display()

def main(filename: str):
    p1(filename)

if __name__ == "__main__":
    main(argv[1])
