"""
Author: Jeomhps
Date  : 2024-12-10
AoC 2024 Day 09 - https://adventofcode.com/2024/day/09
"""

from sys import argv


def p1(text) -> int:
    text = text.replace('\n', '')

    result_list = []
    file_id = 0
    for i in range(len(text)):
        count = int(text[i])
        if i % 2 == 0:
            result_list.extend([file_id] * count)
            file_id += 1
        else:
            result_list.extend(['.'] * count)

    result = result_list.copy()
    for _ in range(result.count('.')):
        for j in range(len(result) - 1, -1, -1):
            if result[j] != ".":
                first_dot = result.index(".")
                if first_dot < j:
                    result[first_dot], result[j] = result[j], "."
                break

    checksum = 0
    for i, block in enumerate(result):
        if block != ".":
            checksum += i * block

    return checksum

def p2(text) -> int:
    sum = 0;
    return sum

def main(filename: str):
    with open(filename, 'r') as file:
        text = file.read()

    s1 = p1(text)
    s2 = p2(text)
    print(s1,s2)

if __name__ == "__main__":
    main(argv[1])
