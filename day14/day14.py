import copy

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    grid = [list(line) for line in lines]

    for r, row in enumerate(grid):
        for c, space in enumerate(row):
            if space == "O":
                move_rock(grid, r, c, -1, 0)

    for r, row in enumerate(grid):
        total += row.count("O") * (len(grid) - r)

    return total


def move_rock(grid: list[list[str]], r: int, c: int, r_dir: int, c_dir: int):
    move_spaces = 0
    while good_square(grid, r + r_dir + (move_spaces * r_dir), c + c_dir + (move_spaces * c_dir)) and \
            grid[r + r_dir + (move_spaces * r_dir)][c + c_dir + (move_spaces * c_dir)] == ".":
        move_spaces += 1
    if move_spaces > 0:
        grid[r + (move_spaces * r_dir)][c + (move_spaces * c_dir)] = "O"
        grid[r][c] = "."


def good_square(grid: list[list[str]], r: int, c: int) -> bool:
    return 0 <= r <= len(grid) - 1 and 0 <= c <= len(grid[r]) - 1


def solve_part2(lines: list[str]) -> int:
    total = 0

    grid = [list(line) for line in lines]
    cache = {platform_to_string(grid)}
    grids = [copy.deepcopy(grid)]
    for i in range(1000000000):
        cycle(grid)

        grid_str = platform_to_string(grid)
        if grid_str in cache:
            break

        cache.add(grid_str)
        grids.append(copy.deepcopy(grid))

    last = i + 1
    start_loop = grids.index(grid)
    loop_length = last - start_loop
    delta = (1000000000 - start_loop) % loop_length
    for _ in range(delta):
        cycle(grid)

    for r, row in enumerate(grid):
        total += row.count("O") * (len(grid) - r)

    return total


def cycle(grid: list[list[str]]):
    for direction in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
        grid_iterator = reversed(list(enumerate(grid))) if direction[0] == 1 else enumerate(grid)
        for r, row in grid_iterator:
            row_iterator = reversed(list(enumerate(row))) if direction[1] == 1 else enumerate(row)
            for c, space in row_iterator:
                if space == "O":
                    move_rock(grid, r, c, *direction)


def platform_to_string(grid: list[list[str]]) -> str:
    return "".join("".join(row) for row in grid)


if __name__ == '__main__':
    input_lines = readfile("day14/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
