import re

from util.file import readfile

num_re = re.compile("([0-9]+)")


def solve_part1(lines: list[str]) -> int:
    total = 0

    for i, line in enumerate(lines):
        search_results = num_re.findall(line)
        start_find = 0
        for num in search_results:
            loc = line.find(num, start_find)
            start_find = loc + len(num)

            check_lines = get_check_lines(lines, i)
            if find_symbol(check_lines, loc, len(num)):
                total += int(num)

    return total


def get_check_lines(lines: list[str], current_line: int) -> list[str]:
    check_lines = []

    if current_line > 0:
        check_lines.append(lines[current_line - 1])
    check_lines.append(lines[current_line])
    if current_line < (len(lines) - 1):
        check_lines.append(lines[current_line + 1])

    return check_lines


def find_symbol(lines: list[str], loc: int, number_len: int) -> bool:
    found = False

    for line in lines:
        start = loc if loc == 0 else loc - 1
        sub_line = line[start:loc + number_len + 1]
        for c in sub_line:
            if not (c.isnumeric() or c == "."):
                found = True

    return found


def solve_part1_alt(lines: list[str]) -> int:
    total = 0

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c.isnumeric() or c == ".":
                continue
            else:
                check_lines = get_check_lines(lines, i)
                numbers = find_numbers(check_lines, j)
                for k in numbers:
                    total += k

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "*":
                check_lines = get_check_lines(lines, i)
                numbers = find_numbers(check_lines, j)

                if len(numbers) == 2:
                    total += (numbers[0] * numbers[1])

    return total


def find_numbers(lines: list[str], loc: int) -> list[int]:
    numbers = []

    for line in lines:
        search_results = num_re.findall(line)
        start_loc = 0
        for num in search_results:
            num_loc = line.find(num, start_loc)
            start_loc = num_loc + len(num)
            if (num_loc - 1) <= loc <= (num_loc + len(num)):
                numbers.append(int(num))

    return numbers


if __name__ == '__main__':
    input_lines = readfile("day03/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 1(alternate solution): {solve_part1_alt(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
