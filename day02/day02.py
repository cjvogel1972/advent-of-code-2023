import re

from util.file import readfile

game_num_re = re.compile("Game ([0-9]*):")
red_re = re.compile("([0-9]*) red")
blue_re = re.compile("([0-9]*) blue")
green_re = re.compile("([0-9]*) green")


def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        good_grab = True
        game_number = int(game_num_re.findall(line)[0])

        colon_loc = line.index(":")
        grabs = line[colon_loc + 1:].split(";")

        for grab in grabs:
            red = find_number(grab, red_re)
            if red > 12:
                good_grab = False
                break

            green = find_number(grab, green_re)
            if green > 13:
                good_grab = False
                break

            blue = find_number(grab, blue_re)
            if blue > 14:
                good_grab = False
                break

        if good_grab:
            total += game_number

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for line in lines:
        red = 0
        green = 0
        blue = 0

        colon_loc = line.index(":")
        grabs = line[colon_loc + 1:].split(";")

        for grab in grabs:
            red = max(red, find_number(grab, red_re))
            green = max(green, find_number(grab, green_re))
            blue = max(blue, find_number(grab, blue_re))

        total += (red * green * blue)

    return total


def find_number(grab: str, regex: re) -> int:
    number = 0

    result = regex.findall(grab)
    if len(result) > 0:
        number = int(result[0])

    return number


if __name__ == '__main__':
    input_lines = readfile("day02/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
