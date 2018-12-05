# Advent of Code 2018 - Day 2 - Inventory Management System
# https://adventofcode.com/2018/day/2

import sys

def parse_input(lines):
    return [line.strip() for line in lines]

def has_pair(code):
    return has_group(2, code)

def has_triplet(code):
    return has_group(3, code)

def has_group(count, code):
    letters = {}
    for letter in code:
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return count in letters.values()

def part1(codes):
    codes_with_pairs = len([code for code in codes if has_pair(code)])
    codes_with_triplets = len([code for code in codes if has_triplet(code)])
    return codes_with_pairs * codes_with_triplets

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))
