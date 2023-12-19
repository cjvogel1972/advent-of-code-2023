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
    sequence = lines[0].split(",")
    boxes = defaultdict(list)

    for seq in sequence:
        if "=" in seq:
            label, focal = seq.split("=")
            box_number = hash_value(label)
            lenses = boxes[box_number]

            for i, lens in enumerate(lenses):
                if lens[0] == label:
                    lenses[i] = (label, focal)
                    break
            else:
                lenses.append((label, focal))
        else:
            label = seq[:-1]
            box_number = hash_value(label)
            lenses = boxes[box_number]

            for lens in lenses:
                if lens[0] == label:
                    lenses.remove(lens)
                    break

    return sum([sum([focusing_power(box, lens, i) for i, lens in enumerate(lenses)]) for box, lenses in boxes.items()])


def focusing_power(box_number: int, lens: tuple, index: int) -> int:
    return (box_number + 1) * (index + 1) * int(lens[1])


if __name__ == '__main__':
    input_lines = readfile("day15/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
