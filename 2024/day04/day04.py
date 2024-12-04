"""
Author: Jeomhps
Date  : 2024-12-04
AoC 2024 Day 4 - https://adventofcode.com/2024/day/4
"""

from sys import argv


def p1(matrix) -> int:
    """
     S..S..S
     .A.A.A.
     ..MMM..
     SAMXMAS
     ..MMM..
     .A.A.A.
     S..S..S
    """
    patterns = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # Horizontal right
    [(0, 0), (0, -1), (0, -2), (0, -3)],  # Horizontal left
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # Vertical down
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)],  # Vertical up
    [(0, 0), (1, 1), (2, 2), (3, 3)],  # Diagonal down-right
    [(0, 0), (-1, -1), (-2, -2), (-3, -3)],  # Diagonal up-left
    [(0, 0), (1, -1), (2, -2), (3, -3)],  # Diagonal down-left
    [(0, 0), (-1, 1), (-2, 2), (-3, 3)]  # Diagonal up-right
    ]

    rows, cols = len(matrix), len(matrix[0])
    count = 0

    def is_pattern_valid(x, y, pattern):
        """Check if the pattern matches 'XMAS'
        starting at (x, y) using patterns above.
        """
        word = "XMAS"
        for i, (dx, dy) in enumerate(pattern):
            nx, ny = x + dx, y + dy
            if nx < 0 \
               or ny < 0 \
               or nx >= rows \
               or ny >= cols \
               or matrix[nx][ny] != word[i]:
                return False
        return True

    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] == 'X':
                for pattern in patterns:
                    if is_pattern_valid(x, y, pattern):
                        count += 1

    return count


def p2(input) -> int:
    return 0

def main(filename: str):
    with open(filename, 'r') as file:
        matrix = [list(line.strip()) for line in file]

    s1 = p1(matrix)
    print(s1)
    # s2 = p2(lines)
    # print(s1,s2)

if __name__ == "__main__":
    main(argv[1])
