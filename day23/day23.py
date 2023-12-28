import sys

from util.file import readfile
from util.grid import good_square


def solve_part1(lines: list[str]) -> int:
    sys.setrecursionlimit(10000)
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

        longest_path = []
        if self.neighbors:
            possible_paths = []
            for n in self.neighbors:
                possible_paths.append(nodes[n].find_longest_path(nodes))

            if possible_paths:
                longest_path = max(possible_paths, key=len)
                longest_path.append(self)

        if not longest_path:
            longest_path.append(self)
        self.path = longest_path.copy()
        return longest_path


def solve_part2(lines: list[str]) -> int:
    total = 0

    return total


if __name__ == '__main__':
    input_lines = readfile("day23/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
