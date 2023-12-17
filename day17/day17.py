from heapq import heappop, heappush

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    grid = [list(map(int, row)) for row in lines]

    # heat loss, location, direction, steps in direction
    steps = [(0, (0, 0), (0, 0), 0)]

    return compute_min_heat_loss(grid, steps, compute_next_steps_part1)


def compute_min_heat_loss(grid: list[list[int]], steps: list[tuple], next_steps) -> int:
    end = (len(grid) - 1, len(grid[0]) - 1)
    seen = set()

    result = 0
    while steps:
        heat_loss, location, direction, distance = heappop(steps)

        if location == end:
            result = heat_loss
            break

        if location[0] < 0 or location[0] >= len(grid) or location[1] < 0 or location[1] >= len(grid[0]):
            continue

        if (location, direction, distance) in seen:
            continue

        seen.add((location, direction, distance))

        new_steps = next_steps(grid, heat_loss, *location, *direction, distance)
        for step in new_steps:
            heappush(steps, step)

    return result


def compute_next_steps_part1(grid: list[list[int]], heat_loss, r, c, dr, dc, dist: int) -> list[tuple]:
    steps = []

    if r > 0:
        new_distance = dist + 1 if dr == -1 else 1
        if dr != 1 and new_distance <= 3:
            nr = r - 1
            nc = c
            steps.append((heat_loss + grid[nr][nc], (nr, nc), (-1, 0), new_distance))
    if r < len(grid) - 1:
        new_distance = dist + 1 if dr == 1 else 1
        if dr != -1 and new_distance <= 3:
            nr = r + 1
            nc = c
            steps.append((heat_loss + grid[nr][nc], (nr, nc), (1, 0), new_distance))
    if c > 0:
        new_distance = dist + 1 if dc == -1 else 1
        if dc != 1 and new_distance <= 3:
            nr = r
            nc = c - 1
            steps.append((heat_loss + grid[nr][nc], (nr, nc), (0, -1), new_distance))
    if c < len(grid[0]) - 1:
        new_distance = dist + 1 if dc == 1 else 1
        if dc != -1 and new_distance <= 3:
            nr = r
            nc = c + 1
            steps.append((heat_loss + grid[nr][nc], (nr, nc), (0, 1), new_distance))

    return steps


def solve_part2(lines: list[str]) -> int:
    grid = [list(map(int, row)) for row in lines]

    # heat loss, location, direction, steps in direction
    steps = compute_next_steps_part1(grid, 0, 0, 0, 0, 0, 0)

    return compute_min_heat_loss(grid, steps, compute_next_steps_part2)


def compute_next_steps_part2(grid: list[list[int]], heat_loss, r, c, dr, dc, dist: int) -> list[tuple]:
    steps = []

    if r > 0:
        new_distance = dist + 1 if dr == -1 else 1
        if dr == 0 and dist < 4:
            pass
        elif dr != 1 and new_distance <= 10:
            nr = r - 1
            nc = c
            steps.append((heat_loss + grid[nr][nc], (nr, nc), (-1, 0), new_distance))
    if r < len(grid) - 1:
        new_distance = dist + 1 if dr == 1 else 1
        if dr == 0 and dist < 4:
            pass
        elif dr != -1 and new_distance <= 10:
            nr = r + 1
            nc = c
            steps.append((heat_loss + grid[nr][nc], (nr, nc), (1, 0), new_distance))
    if c > 0:
        new_distance = dist + 1 if dc == -1 else 1
        if dc == 0 and dist < 4:
            pass
        elif dc != 1 and new_distance <= 10:
            nr = r
            nc = c - 1
            steps.append((heat_loss + grid[nr][nc], (nr, nc), (0, -1), new_distance))
    if c < len(grid[0]) - 1:
        new_distance = dist + 1 if dc == 1 else 1
        if dc == 0 and dist < 4:
            pass
        elif dc != -1 and new_distance <= 10:
            nr = r
            nc = c + 1
            steps.append((heat_loss + grid[nr][nc], (nr, nc), (0, 1), new_distance))

    return steps


if __name__ == '__main__':
    input_lines = readfile("day17/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
