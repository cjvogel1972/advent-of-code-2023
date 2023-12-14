from util.file import readfile_blocks


def solve_part1(blocks: list[str]) -> int:
    total = 0

    for block in blocks:
        lines = block.splitlines()

        mirror_start = -1
        for i in range(len(lines) - 1):
            if check_mirroring(lines, i):
                mirror_start = i + 1
                break

        if mirror_start != -1:
            total += mirror_start * 100
            continue

        vertical = list(map("".join, zip(*lines)))
        for i in range(len(vertical) - 1):
            if check_mirroring(vertical, i):
                mirror_start = i + 1
                break

        if mirror_start != -1:
            total += mirror_start
            continue

    return total


def check_mirroring(lines: list[str], mirror_start: int) -> bool:
    max_lines = len(lines)
    top = mirror_start
    bottom = mirror_start + 1
    while top >= 0 and bottom < max_lines:
        if lines[top] != lines[bottom]:
            return False
        top -= 1
        bottom += 1

    return True


def solve_part2(blocks: list[str]) -> int:
    total = 0

    for block in blocks:
        lines = block.splitlines()

        mirror_start = -1
        for i in range(len(lines) - 1):
            if check_mirroring_smudge(lines, i):
                mirror_start = i
                break

        if mirror_start != -1:
            total += (mirror_start + 1) * 100
            continue

        vertical = list(map("".join, zip(*lines)))
        for i in range(len(vertical) - 1):
            if check_mirroring_smudge(vertical, i):
                mirror_start = i
                break

        if mirror_start != -1:
            total += mirror_start + 1
            continue

    return total


def check_mirroring_smudge(lines: list[str], mirror_start: int) -> bool:
    max_lines = len(lines)
    top = mirror_start
    bottom = mirror_start + 1
    diffs = 0
    while top >= 0 and bottom < max_lines:
        if lines[top] != lines[bottom]:
            diffs += count_diffs(lines[top], lines[bottom])
        top -= 1
        bottom += 1

    return diffs == 1


def count_diffs(line1: str, line2: str) -> int:
    count = 0
    for c1, c2 in zip(line1, line2):
        if c1 != c2:
            count += 1

    return count


if __name__ == '__main__':
    input_lines = readfile_blocks("day13/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
