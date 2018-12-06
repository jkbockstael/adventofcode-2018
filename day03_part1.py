# Advent of Code 2018 - Day 3 - No Matter How You Slice It
# https://adventofcode.com/2018/day/3

import sys
import re

def parse_input(lines):
    claims = []
    for line in lines:
        match = re.match(r"#(?P<id>\d+) @ (?P<left>\d+),(?P<top>\d+): (?P<width>\d+)x(?P<height>\d+)", line)
        claims.append(match.groupdict())
    return claims

def map_claims(claims):
    claims_map = [[[] for x in range(1000)] for y in range(1000)]
    for claim in claims:
        for x in range(int(claim["left"]), int(claim["left"]) + int(claim["width"])):
            for y in range(int(claim["top"]), int(claim["top"]) + int(claim["height"])):
                claims_map[x][y].append(int(claim["id"]))
    return claims_map

def count_overlaps(claims_map):
    overlaps = 0
    for x in range(1000):
        for y in range(1000):
            if len(claims_map[x][y]) > 1:
                overlaps += 1
    return overlaps

def part1(claims):
    return count_overlaps(map_claims(claims))

print(part1(parse_input(sys.stdin.readlines())))
