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


def p2(matrix) -> int:
    """
    possible patterns :

    M.S M.M S.M S.S
    .A. .A. .A. .A.
    M.S S.S S.M M.M

    My idea to solve this is for each char, take the relevant chars using an 
    offset to concatenate them and check wheter the concatenation is exactly
    the same as the concat of one of the possibility.
    """

    target_patterns = {"MSAMS", "MMASS", "SMASM", "SSAMM"}

    rows, cols = len(matrix), len(matrix[0])

    offsets = [
        (0, 0), # Current char
        (0, 2), # Cols + 2 char so top right of scheme
        (1, 1), # Middle one, the A
        (2, 0), # Bottom left one
        (2, 2), # Bottom right one
    ]

    xmas_count = 0

    for r in range(rows):
        for c in range(cols):
            if all(0 <= r + dr < rows and 0 <= c + dc < cols for dr, dc in offsets):
                pattern = "".join(matrix[r + dr][c + dc] for dr, dc in offsets)

                if pattern in target_patterns:
                    xmas_count += 1

    return xmas_count

def main(filename: str):
    with open(filename, 'r') as file:
        matrix = [list(line.strip()) for line in file]

    s1 = p1(matrix)
    s2 = p2(matrix)
    print(s1,s2)

if __name__ == "__main__":
    main(argv[1])
