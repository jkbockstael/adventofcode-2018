# Advent of Code 2018 - Day 3 - No Matter How You Slice It - Part 2
# https://adventofcode.com/2018/day/3

import sys
from day03_part1 import parse_input, map_claims

def find_good_claim(claims):
    claims_map = map_claims(claims)
    claim_ids = [int(claim["id"]) for claim in claims]
    for x in range(1000):
        for y in range(1000):
            if len(claims_map[x][y]) > 1:
                for claim_id in claims_map[x][y]:
                    if claim_id in claim_ids:
                        claim_ids.remove(claim_id)
    return claim_ids[0]

def part2(claims):
    return find_good_claim(claims)

print(part2(parse_input(sys.stdin.readlines())))
