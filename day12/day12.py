from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        springs, records = line.split()
        records = list(map(int, records.split(",")))

        total += count_possibilities(springs, records)

    return total


def memoize(f):
    fast = {}

    def partner(springs: str, records: list[int]):
        r = tuple(records)
        if (springs, r) not in fast:
            fast[(springs, r)] = f(springs, records)
        return fast[(springs, r)]

    return partner


@memoize
def count_possibilities(springs: str, records: list[int]) -> int:
    result = 0
    if springs == "":
        return 1 if len(records) == 0 else 0
    if len(records) == 0:
        return 1 if springs.count("#") == 0 else 0
    if springs[0] in '.?':
        result += count_possibilities(springs[1:], records)
    if springs[0] in '#?':
        if len(springs) >= records[0] and springs[:records[0]].count(".") == 0 and (
                records[0] == len(springs) or springs[records[0]] != '#'):
            result += count_possibilities(springs[records[0] + 1:], records[1:])

    return result


def solve_part2(lines: list[str]) -> int:
    total = 0

    for i, line in enumerate(lines):
        springs, records = line.split()
        records = list(map(int, records.split(",")))

        total += unfold_and_count_possibilities(springs, records)

    return total


def unfold_and_count_possibilities(springs: str, records: list[int]) -> int:
    return count_possibilities(*unfold(springs, records))


def unfold(springs: str, records: list[int]) -> (str, list[int]):
    return "?".join([springs] * 5), records * 5


if __name__ == '__main__':
    input_lines = readfile("day12/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
