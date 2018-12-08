# Advent of Code 2018 - Day 5 - Alchemical Reduction - Part 2
# https://adventofcode.com/2018/day/5

import sys
from day05_part1 import parse_input, reduce_polymer

def remove_unit(unit, polymer):
    return polymer.replace(unit, '').replace(unit.upper(), '')
    
def part2(polymer):
    units = set(polymer.lower())
    best_reduction = len(polymer)
    for unit in units:
        stripped_polymer = remove_unit(unit, polymer)
        reduced_polymer = reduce_polymer(stripped_polymer)
        best_reduction = min(best_reduction, len(reduced_polymer))
    return best_reduction
    
print(part2(parse_input(sys.stdin.readlines())))
