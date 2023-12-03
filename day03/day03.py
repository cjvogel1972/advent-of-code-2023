import re

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0
    num_re = re.compile("([0-9]+)")

    for i in range(len(lines)):
        line = lines[i]
        search_results = num_re.findall(line)
        start_find = 0
        for result in search_results:
            loc = line.find(result, start_find)
            start_find = loc + len(result)

            check_lines = []
            if i > 0:
                check_lines.append(lines[i - 1])
            check_lines.append(line)
            if i < (len(lines) - 1):
                check_lines.append(lines[i + 1])

            if find_symbol(check_lines, loc, len(result)):
                total += int(result)

    return total


def find_symbol(lines: list[str], loc: int, number_len: int) -> bool:
    found = False

    for line in lines:
        start = loc - 1
        if loc == 0:
            start = loc
        sub_line = line[start:loc + number_len + 1]
        for c in sub_line:
            if not (c.isnumeric() or c == "."):
                found = True

    return found


def solve_part1_alt(lines: list[str]) -> int:
    total = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            c = lines[i][j]
            if c.isnumeric() or c == ".":
                continue
            else:
                check_lines = []
                if i > 0:
                    check_lines.append(lines[i - 1])
                check_lines.append(lines[i])
                if i < (len(lines) - 1):
                    check_lines.append(lines[i + 1])

                numbers = find_numbers(check_lines, j)
                for k in numbers:
                    total += k

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for i in range(len(lines)):
        for j in range(len(lines[i])):
            c = lines[i][j]
            if c == "*":
                check_lines = []
                if i > 0:
                    check_lines.append(lines[i - 1])
                check_lines.append(lines[i])
                if i < (len(lines) - 1):
                    check_lines.append(lines[i + 1])

                numbers = find_numbers(check_lines, j)

                if len(numbers) == 2:
                    total += (numbers[0] * numbers[1])

    return total


def find_numbers(lines: list[str], loc: int) -> list[int]:
    result = []

    num_re = re.compile("([0-9]+)")

    for line in lines:
        search_results = num_re.findall(line)
        start_loc = 0
        for num in search_results:
            num_loc = line.find(num, start_loc)
            start_loc = num_loc + len(num)
            if (num_loc - 1) <= loc <= (num_loc + len(num)):
                result.append(int(num))

    return result


if __name__ == '__main__':
    input_lines = readfile("day03/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 1(alternate solution): {solve_part1_alt(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
