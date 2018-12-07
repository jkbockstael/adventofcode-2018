# Advent of Code 2018 - Day 4 - Repose Record
# https://adventofcode.com/2018/day/4

import sys

def parse_input(lines):
    lines.sort()
    naps_map = {}
    for line in lines:
        date = line[1:11]
        hour = line[12:14]
        minute = line[15:17]
        event = line[19:]
        if event.startswith("Guard"):
            guard = int(event.split(" ")[1][1:])
            continue
        if event.startswith("falls asleep"):
            naptime = int(minute)
            continue
        if event.startswith("wakes up"):
            waketime = int(minute)
            if date not in naps_map:
                naps_map[date] = {"guard": guard, "naps": [0 for _ in range(60)]}
            for x in range(naptime, waketime):
                naps_map[date]["naps"][x] = 1
    return naps_map

def get_naps_for_guard(naps_map, guard):
    logs = [naps_map[x] for x in naps_map if naps_map[x]["guard"] == guard]
    return list(zip(*[x["naps"] for x in logs]))

def part1(naps_map):
    guards = set([x["guard"] for x in naps_map.values()])
    best_guard = None
    best_minute = None
    best_total = 0
    for guard in guards:
        naps = get_naps_for_guard(naps_map, guard)
        naps_total = sum([sum(x) for x in naps])
        if naps_total > best_total:
            best_total = naps_total
            best_guard = guard
    best_overlap = 0
    for minute in range(60):
        naps = get_naps_for_guard(naps_map, best_guard)
        if sum(naps[minute]) > best_overlap:
            best_overlap = sum(naps[minute])
            best_minute = minute
    return best_guard * best_minute

print(part1(parse_input(sys.stdin.readlines())))
