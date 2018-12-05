# Advent of Code 2018 - Day 1 - Chronal Calibration - Part 2
# https://adventofcode.com/2018/day/1

import sys
from day01_part1 import parse_input

def part2(changes):
    current_frequency = 0
    reached_frequencies = [0]
    while True:
        for change in changes:
            current_frequency += change
            if current_frequency in reached_frequencies:
                return current_frequency
            else:
                reached_frequencies.append(current_frequency)

print(part2(parse_input(sys.stdin.readlines())))
