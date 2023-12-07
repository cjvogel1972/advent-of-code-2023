from util.file import readfile_blocks


def solve_part1(blocks: list[str]) -> int:
    seeds_input, *others = blocks
    seeds = list(map(int, seeds_input.split(":")[1].split()))

    mappings = parse_mapping_blocks(others)

    values = []
    for seed in seeds:
        value = seed
        for mapping_list in mappings:
            value = map_value(value, mapping_list)

        values.append(value)

    return min(values)


def parse_mapping_blocks(blocks):
    mappings = []

    for block in blocks:
        current_mapping = []
        for line in block.splitlines()[1:]:
            current_mapping.append(Mapping(*list(map(int, line.split()))))
        mappings.append(current_mapping)

    return mappings


def map_value(value, mappings):
    for m in mappings:
        if m.source <= value <= m.source_end:
            return m.map_source_value(value)
    return value


def solve_part2(blocks: list[str]) -> int:
    seeds_input, *others = blocks
    seeds_input = list(map(int, seeds_input.split(":")[1].split()))
    seeds = [SeedRange(seeds_input[i], seeds_input[i + 1]) for i in range(0, len(seeds_input), 2)]

    mappings = parse_mapping_blocks(others)

    values = []
    for seed in seeds:
        ranges = [(seed.start, seed.end)]
        for mapping_list in mappings:
            ranges = ranges_all_mappings(ranges, mapping_list)

        values.append(min(ranges)[0])

    return min(values)


def ranges_all_mappings(ranges, mappings):
    answer = []
    for m in mappings:
        new_ranges = []
        for r in ranges:
            start, end = r
            overlap = (max(start, m.source), min(m.source_end, end))
            if overlap[1] > overlap[0]:
                answer.append((m.map_source_value(overlap[0]), m.map_source_value(overlap[1])))
                before = (start, overlap[0])
                if before[1] > before[0]:
                    new_ranges.append(before)
                after = (overlap[1], end)
                if after[1] > after[0]:
                    new_ranges.append(after)
            else:
                new_ranges.append((start, end))
        ranges = new_ranges
    return answer + ranges


class Mapping:
    def __init__(self, dest: int, source: int, size: int):
        self.dest = dest
        self.dest_end = self.dest + size
        self.source = source
        self.source_end = self.source + size

    def map_source_value(self, value: int) -> int:
        return self.dest + value - self.source


class SeedRange:
    def __init__(self, start: int, size: int):
        self.start = start
        self.end = start + size


if __name__ == '__main__':
    input_blocks = readfile_blocks("day05/input.txt")

    print(f'Part 1: {solve_part1(input_blocks)}')
    print(f'Part 2: {solve_part2(input_blocks)}')
