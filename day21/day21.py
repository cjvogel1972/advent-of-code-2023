from util.file import readfile
from util.grid import good_square


def solve_part1(lines: list[str], steps_needed: int) -> int:
    grid = [list(line) for line in lines]

    start = (0, 0)
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == 'S':
                start = (r, c)
                break
        else:
            continue
        break

    end_location = set()
    seen = set()
    next_steps = [(start, 0)]
    while next_steps:
        next_step = next_steps.pop()
        loc, steps = next_step
        if steps == steps_needed:
            end_location.add(loc)
            continue

        if next_step in seen:
            continue

        seen.add(next_step)

        r, c = loc
        for dr, dc in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            nr = r + dr
            nc = c + dc
            if not good_square(grid, nr, nc) or grid[nr][nc] == '#':
                continue

            next_steps.insert(0, ((nr, nc), steps + 1))

    return len(end_location)


def solve_part2(lines: list[str], steps_needed: int) -> int:
    total = 0

    return total


if __name__ == '__main__':
    input_lines = readfile("day21/input.txt")

    print(f'Part 1: {solve_part1(input_lines, 64)}')
    print(f'Part 2: {solve_part2(input_lines, 26501365)}')
