from util.file import readfile
from util.grid import manhattan_distance


def solve(lines: list[str], expansion: int) -> int:
    galaxies = find_galaxies(lines)
    expand_universe(galaxies, lines, expansion)
    return compute_total_shortest_distance(galaxies)


def find_galaxies(lines: list[str]):
    galaxies = []

    for r, row in enumerate(lines):
        start_loc = 0
        while row.count('#', start_loc) > 0:
            c = row.index("#", start_loc)
            galaxies.append((r, c))
            start_loc = c + 1

    return galaxies


def expand_universe(galaxies: list[tuple[int, int]], lines: list[str], expansion: int):
    for r, row in reversed(list(enumerate(lines))):
        if row.count('.') == len(row):
            for g, galaxy in enumerate(galaxies):
                if galaxy[0] > r:
                    galaxies[g] = (galaxy[0] + expansion - 1, galaxy[1])

    cols = zip(*lines)
    for c, col in reversed(list(enumerate(cols))):
        if col.count('.') == len(col):
            for g, galaxy in enumerate(galaxies):
                if galaxy[1] > c:
                    galaxies[g] = (galaxy[0], galaxy[1] + expansion - 1)


def compute_total_shortest_distance(galaxies) -> int:
    total = 0

    for g, g1 in enumerate(galaxies[:-1]):
        total += sum([manhattan_distance(g1, g2) for g2 in galaxies[g + 1:]])

    return total


if __name__ == '__main__':
    input_lines = readfile("day11/input.txt")

    print(f'Part 1: {solve(input_lines, 2)}')
    print(f'Part 2: {solve(input_lines, 1000000)}')
