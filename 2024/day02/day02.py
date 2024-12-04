"""
Author: Jeomhps
Date  : 2024-12-04
AoC 2024 Day 2 - https://adventofcode.com/2024/day/2
"""

from sys import argv

with open(argv[1], 'r') as file:
    lines = file.readlines()

def p1() -> int:
    nb_safe_report = 0

    for line in lines:
        columns = list(map(int, line.strip().split(' ')))
        if (columns == sorted(columns) or columns == sorted(columns, reverse = True)):
            is_valid = True
            for i in range(len(columns) - 1):
                difference = abs(columns[i+1] - columns[i])
                if (difference < 1 or difference > 3):
                    is_valid = False
                    break

            if is_valid:
                nb_safe_report += 1

    return nb_safe_report

def p2() -> int:
    return 0


def main(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()

    s1 = p1()
    print(s1)

if __name__ == "__main__":
    main(argv[1])
