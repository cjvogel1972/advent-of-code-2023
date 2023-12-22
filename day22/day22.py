from copy import deepcopy

from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    bricks = []
    for line in lines:
        bricks.append(Brick(line))

    bricks.sort(key=lambda brick: min(brick.z1, brick.z2))
    drop_bricks(bricks)

    for i, brick1 in enumerate(bricks):
        for brick2 in bricks[i + 1:]:
            if brick2.directly_above(brick1) and brick2.overlap(brick1):
                brick1.above.append(brick2)
                brick2.below.append(brick1)

    disintegrate = []

    for i, brick1 in enumerate(bricks):
        if brick1.can_disintegrate():
            disintegrate.append(brick1)

    return len(disintegrate)


class Brick:
    def __init__(self, line: str):
        b1, b2 = line.split('~')
        self.y1, self.x1, self.z1 = map(int, b1.split(','))
        self.y2, self.x2, self.z2 = map(int, b2.split(','))
        self.below = []
        self.above = []

    def drop(self):
        self.z1 -= 1
        self.z2 -= 1

    def on_ground(self) -> bool:
        return self.z1 == 1 or self.z2 == 1

    def directly_above(self, brick2) -> bool:
        return self.z1 - 1 == brick2.z1 or self.z2 - 1 == brick2.z1 or self.z1 - 1 == brick2.z2 or self.z2 - 1 == brick2.z2

    def overlap(self, brick2) -> bool:
        y_max = max(self.y1, self.y2)
        x_max = max(self.x1, self.x2)
        y_min = min(self.y1, self.y2)
        x_min = min(self.x1, self.x2)
        b2_y_max = max(brick2.y1, brick2.y2)
        b2_x_max = max(brick2.x1, brick2.x2)
        b2_y_min = min(brick2.y1, brick2.y2)
        b2_x_min = min(brick2.x1, brick2.x2)

        dx = min(x_max, b2_x_max) - max(x_min, b2_x_min)
        dy = min(y_max, b2_y_max) - max(y_min, b2_y_min)

        return dx >= 0 and dy >= 0

    def can_disintegrate(self) -> bool:
        if len(self.above) == 0:
            return True

        for brick in self.above:
            if len(brick.below) == 1:
                return False

        return True

    def __repr__(self):
        return f"{self.y1},{self.x1},{self.z1}~{self.y2},{self.x2},{self.z2}"


def drop_bricks(bricks: list[Brick]) -> int:
    dropped_bricks = set()
    for i, brick1 in enumerate(bricks):
        if brick1.on_ground():
            continue

        can_drop = True
        while can_drop:
            if brick1.on_ground():
                break

            for j, brick2 in enumerate(bricks):
                if i == j:
                    continue

                if brick1.directly_above(brick2):
                    if brick1.overlap(brick2):
                        can_drop = False
                        break

            if can_drop:
                brick1.drop()
                dropped_bricks.add(brick1)

    return len(dropped_bricks)


def solve_part2(lines: list[str]) -> int:
    total = 0

    bricks = []
    for line in lines:
        bricks.append(Brick(line))

    bricks.sort(key=lambda brick: min(brick.z1, brick.z2))
    drop_bricks(bricks)

    for i in range(len(lines)):
        bricks_copy = deepcopy(bricks)
        print(i)

        for j, brick1 in enumerate(bricks_copy):
            for brick2 in bricks_copy[j + 1:]:
                if brick2.directly_above(brick1) and brick2.overlap(brick1):
                    brick1.above.append(brick2)
                    brick2.below.append(brick1)

        if not bricks_copy[i].can_disintegrate() and len(bricks_copy[i].above) > 0:
            bricks_copy.pop(i)
            total += drop_bricks(bricks_copy)

    return total


if __name__ == '__main__':
    input_lines = readfile("day22/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
