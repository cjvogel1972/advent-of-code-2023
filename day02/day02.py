import re

from util.file import readfile

game_num_re = re.compile("Game ([0-9]*):")
cube_re = re.compile("([0-9]*) (red|green|blue)")


def solve_part1(lines: list[str]) -> int:
    total = 0

    max_colors = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    for line in lines:
        good_grab = True
        game_number = int(game_num_re.findall(line)[0])

        result = cube_re.findall(line)
        for grab in result:
            if int(grab[0]) > max_colors[grab[1]]:
                good_grab = False
                break

        if good_grab:
            total += game_number

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for line in lines:
        max_colors = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }

        result = cube_re.findall(line)
        for grab in result:
            if int(grab[0]) > max_colors[grab[1]]:
                max_colors[grab[1]] = int(grab[0])

        power = 1
        for x in max_colors.values(): power *= x
        total += power

    return total


if __name__ == '__main__':
    input_lines = readfile("day02/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
