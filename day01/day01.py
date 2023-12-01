from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    answer = 0
    for line in lines:
        num = ""
        for i in line:
            if i.isnumeric():
                num += i
        num = num[0] + num[len(num) - 1]
        answer += int(num)

    return answer


def solve_part2(lines: list[str]) -> int:
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

    answer = 0
    for line in lines:
        num = ""
        for i in range(len(line)):
            for name in words_to_numbers:
                if line.find(name, i, i + len(name)) != -1:
                    num += words_to_numbers[name]
                elif line[i].isnumeric():
                    num += line[i]
        num = num[0] + num[len(num) - 1]
        answer += int(num)

    return answer


if __name__ == '__main__':
    lines = readfile("day01/input.txt")

    print(f'Part 1: {solve_part1(lines)}')
    print(f'Part 2: {solve_part2(lines)}')
