from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    grid, distance = create_grids(lines)
    start = find_start(grid)

    compute_pipe_distances(grid, distance, start)

    return max([max(row) for row in distance])


def create_grids(lines):
    grid = [list(line) for line in lines]
    distance = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    return grid, distance


def find_start(grid: list[list[str]]) -> tuple:
    for r, row in enumerate(grid):
        if row.count('S') == 1:
            return r, row.index('S')

    raise ValueError("Could not find the start of the pipes")


def compute_pipe_distances(grid, distance, start):
    steps = compute_next_steps(grid, *start)
    while steps:
        current = steps.pop()
        new_step = follow_pipe(grid, distance, *current)
        if new_step[1] != (0, 0):
            steps.insert(0, new_step)


def compute_next_steps(grid: list[list[str]], r: int, c: int) -> list[tuple]:
    location = (r, c)
    steps = []

    if r > 0:
        steps.append((location, (-1, 0)))
    if r < len(grid) - 1:
        steps.append((location, (1, 0)))
    if c > 0:
        steps.append((location, (0, -1)))
    if c < len(grid[0]) - 1:
        steps.append((location, (0, 1)))

    return steps


def follow_pipe(grid: list[list[str]], distance: list[list[int]], location: tuple, direction: tuple) -> tuple:
    r, c = location
    ch = grid[r][c]
    dir_r, dir_c = direction
    dist = distance[r][c]
    new_r = r + dir_r
    new_c = c + dir_c

    if not 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
        return (0, 0), (0, 0)

    new_ch = grid[new_r][new_c]
    if new_ch == '.':
        return (0, 0), (0, 0)

    if distance[new_r][new_c] != 0:
        if distance[new_r][new_c] + 1 < dist:
            distance[new_r][new_c] = dist + 1
        return (0, 0), (0, 0)

    if dir_r != 0:
        if new_ch in '|FLJ7':
            distance[new_r][new_c] = dist + 1
        if new_ch == '|':
            return (new_r, new_c), direction
        if new_ch in 'FL':
            return (new_r, new_c), (0, 1)
        if new_ch in 'J7':
            return (new_r, new_c), (0, -1)

    if dir_c != 0:
        if new_ch in ('-', 'F', '7', 'J', 'L'):
            distance[new_r][new_c] = dist + 1
        if new_ch == '-':
            return (new_r, new_c), direction
        if new_ch in ('F', '7'):
            return (new_r, new_c), (1, 0)
        if new_ch in ('J', 'L'):
            return (new_r, new_c), (-1, 0)

    return (0, 0), (0, 0)


def solve_part2(lines: list[str]) -> int:
    grid, distance = create_grids(lines)
    start = find_start(grid)

    compute_pipe_distances(grid, distance, start)

    # get rid of unnecessary pipes
    for r, row in enumerate(distance):
        for c, d in enumerate(row):
            if d == 0 and grid[r][c] != 'S':
                grid[r][c] = '.'
    grid[start[0]][start[1]] = solve_start_pipe(grid, start)

    for r, row in enumerate(grid):
        outside = True
        for c, ch in enumerate(row):
            if ch == '.' and outside:
                grid[r][c] = 'O'
            elif ch == '.' and not outside:
                grid[r][c] = 'I'
            if ch in '|LJ':
                outside = not outside

    return sum([row.count('I') for row in grid])


def solve_start_pipe(grid: list[list[str]], start: tuple) -> str:
    possible_s = {'|', '-', 'F', 'L', 'J', '7'}

    start_row, start_column = start
    if start_row > 0 and grid[start_row - 1][start_column] in '|F7':
        possible_s.intersection_update({'|', 'L', 'J'})
    if start_row < len(grid) - 1 and grid[start_row + 1][start_column] in '|LJ':
        possible_s.intersection_update({'|', 'F', '7'})
    if start_column > 0 and grid[start_row][start_column - 1] in '-LF':
        possible_s.intersection_update({'-', 'J', '7'})
    if start_column < len(grid[0]) - 1 and grid[start_row][start_column + 1] in '-7J':
        possible_s.intersection_update({'-', 'L', 'F'})

    return possible_s.pop()


if __name__ == '__main__':
    input_lines = readfile("day10/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
