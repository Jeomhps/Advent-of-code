"""
Author: Jeomhps
Date  : 2024-12-04
AoC 2024 Day 2 - https://adventofcode.com/2024/day/2
"""

from sys import argv

def is_safe_report(columns):
    """
    encapsulated p1 code in function changed order of verification since for
    part2 it's better to check for level first.
    """
    for i in range(len(columns) - 1):
        difference = abs(columns[i+1] - columns[i])
        if difference < 1 or difference > 3:
            return False
    return columns == sorted(columns) or columns == sorted(columns, reverse=True)


def p1(lines) -> int:
    nb_safe_report = 0

    for line in lines:
        columns = list(map(int, line.strip().split(' ')))
        
        if(is_safe_report(columns)):
            nb_safe_report += 1

        # if (columns == sorted(columns) or columns == sorted(columns, reverse = True)):
        #     is_valid = True
        #     for i in range(len(columns) - 1):
        #         difference = abs(columns[i+1] - columns[i])
        #         if (difference < 1 or difference > 3):
        #             is_valid = False
        #             break
        #
        #     if is_valid:
        #         nb_safe_report += 1

    return nb_safe_report

def p2(lines) -> int:
    nb_safe_report = 0

    for line in lines:
        columns = list(map(int, line.strip().split(' ')))

        if is_safe_report(columns):
            nb_safe_report += 1
        else:
            """
            If a report is note safe I try to recheck if it's safe by removing
            each element 1 by 1 and recheck whether it is now safe.
            """
            safe_aft_modif = False
            for i in range(len(columns)):
                modified_columns = columns.copy()
                del modified_columns[i]

                if is_safe_report(modified_columns):
                    safe_aft_modif = True
                    break

            if safe_aft_modif:
                nb_safe_report += 1

    return nb_safe_report


def main(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()

    s1 = p1(lines)
    s2 = p2(lines)
    print(s1, s2)

if __name__ == "__main__":
    main(argv[1])
