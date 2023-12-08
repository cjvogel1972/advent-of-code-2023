import re
from math import lcm

from util.file import readfile

node_re = re.compile("([A-Z0-9]+) = \\(([A-Z0-9]+), ([A-Z0-9]+)\\)")


def solve_part1(lines: list[str]) -> int:
    directions, nodes = parse_directions_nodes(lines)

    curr_node = nodes['AAA']
    moves = compute_moves(curr_node, directions, nodes, part1_at_end_check)

    return moves


def part1_at_end_check(name: str) -> bool:
    return name == 'ZZZ'


def solve_part2(lines: list[str]) -> int:
    directions, nodes = parse_directions_nodes(lines)

    curr_nodes = []
    for name in nodes.keys():
        if name[-1] == 'A':
            curr_nodes.append(nodes[name])

    all_moves = []
    for curr_node in curr_nodes:
        moves = compute_moves(curr_node, directions, nodes, part2_at_end_check)
        all_moves.append(moves)

    return lcm(*all_moves)


def part2_at_end_check(name: str) -> bool:
    return name[-1] == 'Z'


def parse_directions_nodes(lines):
    directions = lines[0]
    nodes = {}
    for i in range(2, len(lines)):
        node = Node(lines[i])
        nodes[node.name] = node

    return directions, nodes


def compute_moves(curr_node, directions, nodes, end_check):
    at_end = False
    moves = 0
    while not at_end:
        for d in directions:
            if d == 'L':
                curr_node = nodes[curr_node.left]
            else:
                curr_node = nodes[curr_node.right]

            moves += 1

            if end_check(curr_node.name):
                at_end = True
                break

    return moves


class Node:
    def __init__(self, line: str):
        self.name, self.left, self.right = node_re.findall(line)[0]


if __name__ == '__main__':
    input_lines = readfile("day08/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
