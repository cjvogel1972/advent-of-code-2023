import re

from util.file import readfile

number_re = re.compile("([0-9]+)")


def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        winners = number_card_winners(line)

        if winners > 0:
            total += int(pow(2, (winners - 1)))

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    card_instances = [1 for _ in lines]

    for i, line in enumerate(lines):
        winners = number_card_winners(line)

        for j in range(winners):
            card_instances[i + j + 1] += 1 * card_instances[i]

    total = sum(card_instances)

    return total


def number_card_winners(line: str) -> int:
    colon_loc = line.find(":")
    bar_loc = line.find("|")

    winning_numbers = number_re.findall(line, colon_loc + 1, bar_loc)
    my_numbers = number_re.findall(line, bar_loc + 1)

    winners = 0
    for number in my_numbers:
        try:
            winning_numbers.index(number)
            winners += 1
        except ValueError:
            pass

    return winners


if __name__ == '__main__':
    input_lines = readfile("day04/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
