"""
Author: Jeomhps
Date  : 2024-12-07
AoC 2024 Day 7 - https://adventofcode.com/2024/day/7
"""

from sys import argv

def p1(data) -> list:
    valid_keys = []

    for key, values in data:
        num_operations = len(values) - 1
        
        operator_sequences = []
        for i in range(2 ** num_operations):
            sequence = []
            for _ in range(num_operations):
                if i % 2 == 0:
                    sequence.append('+')
                else:
                    sequence.append('*')
                i //= 2
            operator_sequences.append(sequence)

        for operators in operator_sequences:
            result = values[0]
            
            for i in range(num_operations):
                if operators[i] == '+':
                    result += values[i + 1]
                elif operators[i] == '*':
                    result *= values[i + 1]
            
            if result == key:
                valid_keys.append(key)
                break

    return valid_keys

def p2(text) -> int:
    return 20

def main(filename: str):
    data = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        for line in lines:
            result, values = line.strip().split(":")
            data.append((int(result), list(map(int, values.strip().split()))))

    s1 = p1(data)
    print(sum(s1))
    # s2 = p2(text)
    # print(s1, s2)

if __name__ == "__main__":
    main(argv[1])
