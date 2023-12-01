from util.file import readfile

words_to_numbers = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def solve_part1(lines: list[str]) -> int:
    total = 0

    for line in lines:
        numbers = ""
        for c in line:
            if c.isnumeric():
                numbers += c
        total += int("".join([numbers[0], numbers[-1]]))

    return total


def solve_part2(lines: list[str]) -> int:
    total = 0

    for line in lines:
        numbers = ""
        for i in range(len(line)):
            if line[i].isnumeric():
                numbers += line[i]
            else:
                for name in words_to_numbers:
                    if line[i:i + len(name)] == name:
                        numbers += words_to_numbers[name]
                        break
        total += int("".join([numbers[0], numbers[-1]]))

    return total


if __name__ == '__main__':
    input_lines = readfile("day01/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
