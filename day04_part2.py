# Advent of Code 2018 - Day 4 - Repose Record - Part 2
# https://adventofcode.com/2018/day/4

import sys
from day04_part1 import parse_input, get_naps_for_guard, get_guard_ids

def part2(naps_map):
    guards = get_guard_ids(naps_map)
    best_guard = None
    best_minute = None
    best_overlap = 0
    for guard in guards:
        naps = get_naps_for_guard(naps_map, guard)
        for minute in range(60):
            if sum(naps[minute]) > best_overlap:
                best_overlap = sum(naps[minute])
                best_minute = minute
                best_guard = guard
    return best_guard * best_minute

print(part2(parse_input(sys.stdin.readlines())))
