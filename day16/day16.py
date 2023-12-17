from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    grid = [[x for x in line] for line in lines]

    return determined_number_energized_grids(grid, (0, 0), (0, 1))


def solve_part2(lines: list[str]) -> int:
    max_energized = 0

    grid = [[x for x in line] for line in lines]

    max_rows = len(grid)
    max_cols = len(grid[0])

    for i in range(max_cols):
        energized = determined_number_energized_grids(grid, (0, i), (1, 0))
        max_energized = max(max_energized, energized)
        energized = determined_number_energized_grids(grid, ((max_rows - 1), i), (-1, 0))
        max_energized = max(max_energized, energized)

    for i in range(max_rows):
        energized = determined_number_energized_grids(grid, (i, 0), (0, 1))
        max_energized = max(max_energized, energized)
        energized = determined_number_energized_grids(grid, (i, (max_cols - 1)), (0, -1))
        max_energized = max(max_energized, energized)

    return max_energized


def determined_number_energized_grids(grid: list[list[str]], start: tuple, direction: tuple) -> int:
    energized_grid = [['.' for _ in row] for row in grid]
    seen = set()
    follow_light(grid, energized_grid, seen, start, direction)

    total = 0
    total += sum([sum([1 if x == '#' else 0 for x in row]) for row in energized_grid])

    return total


def follow_light(grid: list[list[str]], energized_grid: list[list[str]], seen: set[tuple], loc: tuple,
                 direction: tuple):
    while True:
        if 0 > loc[0] or loc[0] >= len(grid) or 0 > loc[1] or loc[1] >= len(grid[0]):
            return

        if (loc, direction) in seen:
            return

        seen.add((loc, direction))
        ch = grid[loc[0]][loc[1]]
        energized_grid[loc[0]][loc[1]] = '#'

        if ch == '.':
            loc = (loc[0] + direction[0], loc[1] + direction[1])
        elif ch in '|-':
            if direction[0] != 0 and ch == '|':
                loc = (loc[0] + direction[0], loc[1] + direction[1])
            elif direction[0] != 0 and ch == '-':
                follow_light(grid, energized_grid, seen, (loc[0], loc[1] - 1), (0, -1))
                loc = (loc[0], loc[1] + 1)
                direction = (0, 1)
            elif direction[1] != 0 and ch == '-':
                loc = (loc[0] + direction[0], loc[1] + direction[1])
            elif direction[1] != 0 and ch == '|':
                follow_light(grid, energized_grid, seen, (loc[0] - 1, loc[1]), (-1, 0))
                loc = (loc[0] + 1, loc[1])
                direction = (1, 0)
        elif ch in '/\\':
            if direction[0] == 1 and ch == '\\':
                direction = (0, 1)
                loc = (loc[0], loc[1] + 1)
            elif direction[0] == -1 and ch == '\\':
                direction = (0, -1)
                loc = (loc[0], loc[1] - 1)
            elif direction[1] == 1 and ch == '\\':
                direction = (1, 0)
                loc = (loc[0] + 1, loc[1])
            elif direction[1] == -1 and ch == '\\':
                direction = (-1, 0)
                loc = (loc[0] - 1, loc[1])
            elif direction[0] == 1 and ch == '/':
                direction = (0, -1)
                loc = (loc[0], loc[1] - 1)
            elif direction[0] == -1 and ch == '/':
                direction = (0, 1)
                loc = (loc[0], loc[1] + 1)
            elif direction[1] == 1 and ch == '/':
                direction = (-1, 0)
                loc = (loc[0] - 1, loc[1])
            elif direction[1] == -1 and ch == '/':
                direction = (1, 0)
                loc = (loc[0] + 1, loc[1])


if __name__ == '__main__':
    input_lines = readfile("day16/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
