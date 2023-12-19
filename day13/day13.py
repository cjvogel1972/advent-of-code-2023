from util.file import readfile_blocks


def solve_part1(blocks: list[str]) -> int:
    return summarize_reflections(blocks, check_mirroring)


def summarize_reflections(blocks, check):
    total = 0

    for block in blocks:
        lines = block.splitlines()

        line_of_reflection = find_line_of_reflection(lines, check)

        if line_of_reflection != -1:
            total += line_of_reflection * 100
            continue

        vertical = list(map("".join, zip(*lines)))
        line_of_reflection = find_line_of_reflection(vertical, check)

        if line_of_reflection != -1:
            total += line_of_reflection
            continue

    return total


def find_line_of_reflection(lines: list[str], check):
    line_of_reflection = -1

    for i in range(len(lines) - 1):
        if check(lines, i):
            line_of_reflection = i + 1
            break

    return line_of_reflection


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
    return summarize_reflections(blocks, check_mirroring_smudge)


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
    return sum([1 if c1 != c2 else 0 for c1, c2 in zip(line1, line2)])


if __name__ == '__main__':
    input_lines = readfile_blocks("day13/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
