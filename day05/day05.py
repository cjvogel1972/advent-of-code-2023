import sys

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    seeds = {}
    for i in [int(n) for n in lines[0][6:].split()]:
        seeds[i] = 0

    mappings = {
        "seeds_to_soil": [],
        "soil_to_fertilizer": [],
        "fertilizer_to_water": [],
        "water_to_light": [],
        "light_to_temperature": [],
        "temperature_to_humidity": [],
        "humidity_to_location": []
    }
    mappings_list = list(mappings.keys())
    mapping_index = -1
    skip_next_line = True

    for i, line in enumerate(lines):
        if skip_next_line:
            skip_next_line = False
            continue

        if len(line) == 0:
            mapping_index += 1
            skip_next_line = True
            continue

        nums = [int(n) for n in line.split()]
        mappings[mappings_list[mapping_index]].append(Mapping(*nums))

    for seed in seeds:
        value = seed
        for mapping_list in mappings.values():
            value = map_value(value, mapping_list)

        seeds[seed] = value

    return seeds[min(seeds)]


def map_value(value, mappings):
    for m in mappings:
        if m.source <= value <= m.source + m.size:
            return m.dest + (value - m.source)
    return value


def solve_part2(lines: list[str]) -> int:
    seed_input = [int(n) for n in lines[0][6:].split()]
    seeds = {}
    for i in range(0, len(seed_input), 2):
        seeds[SeedRange(seed_input[i], seed_input[i + 1])] = sys.maxsize

    mappings = {
        "seeds_to_soil": [],
        "soil_to_fertilizer": [],
        "fertilizer_to_water": [],
        "water_to_light": [],
        "light_to_temperature": [],
        "temperature_to_humidity": [],
        "humidity_to_location": []
    }
    mappings_list = list(mappings.keys())
    mapping_index = -1
    skip_next_line = True

    for i, line in enumerate(lines):
        if skip_next_line:
            skip_next_line = False
            continue

        if len(line) == 0:
            mapping_index += 1
            skip_next_line = True
            continue

        nums = [int(n) for n in line.split()]
        mappings[mappings_list[mapping_index]].append(Mapping(*nums))

    for seed in seeds:
        ranges = [(seed.start, seed.start + seed.size)]
        for mapping_list in mappings.values():
            ranges = ranges_all_mappings(ranges, mapping_list)

        seeds[seed] = min(ranges)[0]

    result = sys.maxsize
    for value in seeds.values():
        result = min(result, value)
    return result


def ranges_all_mappings(ranges, mappings):
    answer = []
    for m in mappings:
        my_end = m.source + m.size
        new_ranges = []
        for r in ranges:
            start, end = r
            before = (start, min(end, m.source))
            inside = (max(start, m.source), min(my_end, end))
            after = (max(my_end, start), end)
            if before[1] > before[0]:
                new_ranges.append(before)
            if inside[1] > inside[0]:
                answer.append((m.dest + inside[0] - m.source, m.dest + inside[1] - m.source))
            if after[1] > after[0]:
                new_ranges.append(after)
        ranges = new_ranges
    return answer + new_ranges


class Mapping:
    def __init__(self, dest: int, source: int, size: int):
        self.dest = dest
        self.source = source
        self.size = size


class SeedRange:
    def __init__(self, start: int, size: int):
        self.start = start
        self.size = size


if __name__ == '__main__':
    input_lines = readfile("day05/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
