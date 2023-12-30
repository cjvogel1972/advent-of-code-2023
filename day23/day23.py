from util.file import readfile
from util.grid import good_square


def solve_part1(lines: list[str]) -> int:
    start = (0, lines[0].index('.'))
    end = (len(lines) - 1, lines[-1].index('.'))
    grid = [list(line) for line in lines]

    nodes = find_nodes(grid, start, end)

    return len(nodes[start].find_longest_path(nodes)) - 1


def find_nodes(grid, loc, end, visited=set()) -> dict:
    nodes = {}
    q = [(loc, None)]
    while q:
        loc, prev = q.pop()
        if loc not in visited:
            visited.add(loc)
            node = Node(*loc)
            nodes[loc] = node
            if loc == end:
                continue
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr = loc[0] + direction[0]
                nc = loc[1] + direction[1]
                if not good_square(grid, nr, nc) or grid[nr][nc] == '#' or (nr, nc) == prev:
                    continue
                if (direction == (1, 0) and grid[nr][nc] == '^') or (direction == (-1, 0) and grid[nr][nc] == 'v') or \
                        (direction == (0, 1) and grid[nr][nc] == '<') or (direction == (0, -1) and grid[nr][nc] == '>'):
                    continue
                q.insert(0, ((nr, nc), loc))
                node.neighbors.add((nr, nc))

    return nodes


class Node:
    def __init__(self, r, c: int):
        self.r, self.c = r, c
        self.neighbors = set()
        self.path = []

    def find_longest_path(self, nodes: dict) -> list:
        if self.path:
            return self.path

        current = self
        straight_path = []
        while True:
            longest_path = []
            if current.neighbors:
                if len(current.neighbors) == 1:
                    for n in current.neighbors:
                        current = nodes[n]
                        straight_path.append(current)
                    continue

                possible_paths = []
                for n in current.neighbors:
                    possible_paths.append(nodes[n].find_longest_path(nodes))

                if possible_paths:
                    longest_path = max(possible_paths, key=len)

            current.path = longest_path.copy()
            break

        straight_path.extend(current.path)
        straight_path.insert(0, self)
        self.path = straight_path
        return straight_path

    def __repr__(self):
        return f'Node({self.r},{self.c})'


def solve_part2(lines: list[str]) -> int:
    total = 0

    return total


if __name__ == '__main__':
    input_lines = readfile("day23/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
