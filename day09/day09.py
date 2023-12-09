from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        orig_nums = list(map(int, line.split()))
        diffs = [orig_nums]
        all_zeroes = False
        prev_line = orig_nums
        while not all_zeroes:
            next_diffs = []
            for i in range(len(prev_line) - 1):
                next_diffs.append(prev_line[i + 1] - prev_line[i])
            prev_line = next_diffs
            diffs.append(next_diffs)
            if next_diffs.count(0) == len(next_diffs):
                all_zeroes = True

        diffs[-1].append(0)
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].append(diffs[i][-1] + diffs[i + 1][-1])

        total += diffs[0][-1]

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for line in lines:
        orig_nums = list(map(int, line.split()))
        diffs = [orig_nums]
        all_zeroes = False
        prev_line = orig_nums
        while not all_zeroes:
            next_diffs = []
            for i in range(len(prev_line) - 1):
                next_diffs.append(prev_line[i + 1] - prev_line[i])
            prev_line = next_diffs
            diffs.append(next_diffs)
            if next_diffs.count(0) == len(next_diffs):
                all_zeroes = True

        diffs[-1].insert(0, 0)
        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].insert(0, diffs[i][0] - diffs[i + 1][0])

        total += diffs[0][0]

    return total


if __name__ == '__main__':
    input_lines = readfile("day09/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
