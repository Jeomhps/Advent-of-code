"""
Author: Jeomhps
Date  : 2024-12-04
AoC 2024 Day 3 - https://adventofcode.com/2024/day/3
"""

from sys import argv
# https://www.w3schools.com/python/python_regex.asp
import re


def p1(text) -> int:
    numbers_to_mul = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", text)

    sum = 0
    for a,b in numbers_to_mul:
        sum += (int(a) * int(b))

    return sum

def p2(text) -> int:
    splitted_text = re.split(r"(do\(\)|don't\(\))", text)

    result = []
    keep = True 

    for slice in splitted_text:
        if slice == "do()":
            keep = True
        elif slice == "don't()":
            keep = False
        elif keep:
            result.append(slice)
    
    corrected_text = ''.join(result)

    numbers_to_mul = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", corrected_text)

    sum = 0
    for a,b in numbers_to_mul:
        sum += (int(a) * int(b))

    return sum

def main(filename: str):
    with open(filename, 'r') as file:
        text = file.read()


    s1 = p1(text)
    s2 = p2(text)
    print(s1,s2)

if __name__ == "__main__":
    main(argv[1])
