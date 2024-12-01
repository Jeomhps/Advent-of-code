"""
Author: Jeomhps
Date  : 2024-12-01
AoC 2024 Day 1 - https://adventofcode.com/2024/day/1
"""

from sys import argv

with open(argv[1], 'r') as file:
    lines = file.readlines()

def p1() -> int:
    list1 = []
    list2 = []
    distance_list = []

    for line in lines:
        columns = line.strip().split(',')

        list1.append(int(columns[0]))
        list2.append(int(columns[1]))

    list1.sort()
    list2.sort()

    i = 0;
    for numbers in list1:
        distance_list.append(abs(list2[i] - list1[i]))
        i += 1

    return sum(distance_list)

def p2() -> int:
    hashmap1 = {}
    hashmap2 = {}

    for line in lines:
        columns = line.strip().split(',')

        hashmap1[columns[0]] = hashmap1.get(columns[0], 0) + 1
        hashmap2[columns[1]] = hashmap2.get(columns[1], 0) + 1

    similarity_score = 0
    for key in hashmap1.keys():
        if key in hashmap2.keys():
            similarity_score += (int(key) * hashmap1[key]) * hashmap2[key]

    return similarity_score


def main(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()

    s1 = p1()
    s2 = p2()
    print(s1,s2)

if __name__ == "__main__":
    main(argv[1])
