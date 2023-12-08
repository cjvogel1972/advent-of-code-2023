from math import lcm

from util.file import readfile
import re

node_re = re.compile("([A-Z0-9]+) = \\(([A-Z0-9]+), ([A-Z0-9]+)\\)")


def solve_part1(lines: list[str]) -> int:
    directions = lines[0]
    nodes = {}
    for i in range(2, len(lines)):
        node = Node(lines[i])
        nodes[node.name] = node

    at_end = False
    curr_node = nodes['AAA']
    moves = 0
    while not at_end:
        for d in directions:
            if d == 'L':
                curr_node = nodes[curr_node.left]
            else:
                curr_node = nodes[curr_node.right]
            moves += 1
            if curr_node.name == 'ZZZ':
                at_end = True
                break

    return moves


def solve_part2(lines: list[str]) -> int:
    directions = lines[0]
    nodes = {}
    for i in range(2, len(lines)):
        node = Node(lines[i])
        nodes[node.name] = node

    curr_nodes = []
    for name in nodes.keys():
        if name[-1] == 'A':
            curr_nodes.append(nodes[name])
    all_moves = []
    for curr_node in curr_nodes:
        moves = 0
        at_end = False
        while not at_end:
            for d in directions:
                if d == 'L':
                    curr_node = nodes[curr_node.left]
                else:
                    curr_node = nodes[curr_node.right]
                moves += 1
                if curr_node.name[-1] == 'Z':
                    at_end = True
                    break
        all_moves.append(moves)

    return lcm(*all_moves)


class Node:
    def __init__(self, line: str):
        self.name, self.left, self.right = node_re.findall(line)[0]


if __name__ == '__main__':
    input_lines = readfile("day08/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
