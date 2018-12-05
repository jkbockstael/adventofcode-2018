# Advent of Code 2018 - Day 2 - Inventory Management System
# https://adventofcode.com/2018/day/2

import sys
from day02_part1 import parse_input

def hamming_distance(word1, word2):
    return sum(letter1 != letter2 for letter1, letter2 in zip(word1, word2))

def correct_code_pair(codes):
    for code1 in codes:
        for code2 in codes:
            if hamming_distance(code1, code2) == 1:
                return (code1, code2)

def common_code_part(code1, code2):
    return ''.join([letter1 for letter1, letter2 in zip(code1, code2) if letter1 == letter2])
    
def part2(codes):
    return common_code_part(*correct_code_pair(codes))

print(part2(parse_input(sys.stdin.readlines())))
