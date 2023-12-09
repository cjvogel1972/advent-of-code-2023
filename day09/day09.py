from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        diffs = compute_diffs(list(map(int, line.split())))

        diffs[-1].append(0)
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].append(diffs[i][-1] + diffs[i + 1][-1])

        total += diffs[0][-1]

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for line in lines:
        diffs = compute_diffs(list(map(int, line.split())))

        diffs[-1].insert(0, 0)
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].insert(0, diffs[i][0] - diffs[i + 1][0])

        total += diffs[0][0]

    return total


def compute_diffs(orig_nums: list[int]) -> list[list[int]]:
    diffs = [orig_nums]
    all_zeroes = False
    prev_diffs = diffs[0]

    while not all_zeroes:
        curr_diffs = []
        for i in range(len(prev_diffs) - 1):
            curr_diffs.append(prev_diffs[i + 1] - prev_diffs[i])
        diffs.append(curr_diffs)
        prev_diffs = curr_diffs

        if curr_diffs.count(0) == len(curr_diffs):
            all_zeroes = True

    return diffs


if __name__ == '__main__':
    input_lines = readfile("day09/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
