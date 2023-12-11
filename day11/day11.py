from util.file import readfile


def solve(lines: list[str], expansion: int) -> int:
    galaxies = find_galaxies(lines)
    expand_universe(galaxies, lines, expansion)
    return compute_total_shortest_distance(galaxies)


def find_galaxies(lines):
    galaxies = []

    for r, row in enumerate(lines):
        start_loc = 0
        while row.count('#', start_loc) > 0:
            c = row.index("#", start_loc)
            galaxies.append((r, c))
            start_loc = c + 1
            
    return galaxies


def expand_universe(galaxies, lines, expansion):
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

    for i in range(len(galaxies) - 1):
        g1 = galaxies[i]
        for j in range(i + 1, len(galaxies)):
            g2 = galaxies[j]
            total += abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])

    return total


if __name__ == '__main__':
    input_lines = readfile("day11/input.txt")

    print(f'Part 1: {solve(input_lines, 2)}')
    print(f'Part 2: {solve(input_lines, 1000000)}')
