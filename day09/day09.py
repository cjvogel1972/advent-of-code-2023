from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        diffs = compute_diffs(list(map(int, line.split())))

        value = 0
        for diff in reversed(diffs):
            value = diff[-1] + value

        total += value

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for line in lines:
        diffs = compute_diffs(list(map(int, line.split())))

        value = 0
        for diff in reversed(diffs):
            value = diff[0] - value

        total += value

    return total


def compute_diffs(orig_nums: list[int]) -> list[list[int]]:
    diffs = [orig_nums]
    all_zeroes = False
    prev_diffs = diffs[0]

    while not all_zeroes:
        curr_diffs = [y - x for x, y in zip(prev_diffs, prev_diffs[1:])]

        if curr_diffs.count(0) == len(curr_diffs):
            all_zeroes = True
        else:
            diffs.append(curr_diffs)
            prev_diffs = curr_diffs

    return diffs


if __name__ == '__main__':
    input_lines = readfile("day09/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
