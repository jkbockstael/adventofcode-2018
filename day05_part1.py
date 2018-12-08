# Advent of Code 2018 - Day 5 - Alchemical Reduction
# https://adventofcode.com/2018/day/5

import sys

def parse_input(lines):
    return lines[0].strip()

def is_opposite(character_a, character_b):
    if character_a.islower():
        return character_a.upper() == character_b
    else:
        return character_a.lower() == character_b

def reduce_polymer(polymer):
    reduced = True
    while reduced:
        reduced = False
        for i in range(len(polymer) - 1):
            if is_opposite(polymer[i], polymer[i+1]):
                polymer = polymer[:i] + polymer[i+2:]
                reduced = True
                break
    return polymer

def part1(polymer):
    return len(reduce_polymer(polymer))

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))
