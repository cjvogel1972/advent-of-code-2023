from collections import defaultdict

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    sequence = lines[0].split(",")
    total += sum([hash_value(seq) for seq in sequence])

    return total


def hash_value(value: str) -> int:
    result = 0

    for ch in value:
        result += ord(ch)
        result *= 17
        result %= 256

    return result


def solve_part2(lines: list[str]) -> int:
    total = 0

    sequence = lines[0].split(",")
    boxes = defaultdict(list)

    for seq in sequence:
        if "=" in seq:
            op = "="
            label, focal = seq.split("=")
        else:
            op = "-"
            label = seq.split("-")[0]
        box_number = hash_value(label)
        if boxes[box_number] is None:
            lenses = []
            boxes[box_number] = lenses
        else:
            lenses = boxes[box_number]

        if op == "=":
            for i, lens in enumerate(lenses):
                if lens[0] == label:
                    lenses[i] = (label, focal)
                    break
            else:
                lenses.append((label, focal))
        else:
            for lens in lenses:
                if lens[0] == label:
                    lenses.remove(lens)

    for box_number, lenses in boxes.items():
        total += sum([focusing_power(box_number, lenses, i) for i in range(len(lenses))])

    return total


def focusing_power(box_number: str, lenses: list, index: int) -> int:
    result = int(box_number) + 1
    result *= (index + 1)
    result *= int(lenses[index][1])

    return result


if __name__ == '__main__':
    input_lines = readfile("day15/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
