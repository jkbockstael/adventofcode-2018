# Advent of Code 2018 - Day 1 - Chronal Calibration
# https://adventofcode.com/2018/day/1

import sys

def parse_input(lines):
    return [int(line.strip()) for line in lines]

def part1(changes):
    return sum(changes)

if __name__ == "__main__":
    print(part1(parse_input(sys.stdin.readlines())))
