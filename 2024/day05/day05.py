"""
Author: Jeomhps
Date  : 2024-12-05
AoC 2024 Day 5 - https://adventofcode.com/2024/day/5
"""

from sys import argv

def order(rules, page):
    """ 
    https://stackoverflow.com/questions/21762177/sort-lists-in-python-based-on-a-rule

    This function calculates the "weight" of each item in the 'page' list based on how many rules 
    exist where the item is the key in a tuple (x, y) in the 'rules' set.

    For each item 'x' in the 'page' list:
    - The function counts how many rules exist where 'x' appears as the key in the tuple (x, y), 
    i.e., how many rules are of the form 'x|y'.
    - For example, if the first element in the 'page' list is 47 and there are 2 rules in 'rules' 
    where '47' appears as the key (e.g., "47|53" and "47|61"), then the weight for 47 would be 2.

    The 'page' list is then sorted in **descending order** of these weights. The items with the highest weight 
    come first, and the ones with lower weights are placed later in the sorted list.
    """
    return sorted(page, key=lambda x: -sum(f"{x}|{y}" in rules for y in page))

def p1(rules, pages) -> int:
    mid_sum = 0

    for page in pages:
        sorted_page = order(rules, page)
        middle_value = sorted_page[len(page) // 2]
        if sorted_page == page:
            mid_sum += middle_value

    return mid_sum

def p2(rules, pages) -> int:
    mid_sum = 0

    for page in pages:
        sorted_page = order(rules, page)
        if sorted_page != page:
            middle_value = sorted_page[len(page) // 2]
            mid_sum += middle_value

    return mid_sum

def main(filename: str):
    with open(filename) as file:
        rules, pages = file.read().split('\n\n')

    rules = set(rules.splitlines())
    pages = [list(map(int, line.split(','))) for line in pages.splitlines()]

    s1 = p1(rules, pages)
    s2 = p2(rules, pages)
    print(s1, s2)

if __name__ == "__main__":
    main(argv[1])
