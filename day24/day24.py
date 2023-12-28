from util.file import readfile


def solve_part1(lines: list[str], square_min, square_max: int) -> int:
    total = 0

    hailstones = []
    for line in lines:
        position, velocity = line.split(' @ ')
        hailstones.append((tuple(map(int, position.split(', '))), tuple((map(int, velocity.split(', '))))))

    for i, h1 in enumerate(hailstones):
        for h2 in hailstones[i:]:
            line1 = get_line_equations(h1)
            line2 = get_line_equations(h2)

            if line1[0] == line2[0]:
                continue

            x, y = lines_cross(line1, line2)
            if square_min <= x <= square_max and square_min <= y <= square_max:
                if compute_time_from_x(h1, x) > 0 and compute_time_from_x(h2, x) > 0:
                    total += 1

    return total


def get_line_equations(hail: tuple) -> tuple[int, int]:
    x, y, _ = hail[0]
    vx, vy, _ = hail[1]

    m = vy / vx
    b = y - m * x

    return m, b


def lines_cross(line1: tuple, line2: tuple) -> tuple[int, int]:
    tm = line1[0] - line2[0]
    tb = line2[1] - line1[1]

    x = tb / tm
    y = (line1[0] * x) + line1[1]

    return x, y


def compute_time_from_x(hail: tuple, other_x: int) -> int:
    return (other_x - hail[0][0]) / hail[1][0]


def solve_part2(lines: list[str]) -> int:
    total = 0

    return total


if __name__ == '__main__':
    input_lines = readfile("day24/input.txt")

    print(f'Part 1: {solve_part1(input_lines, 200000000000000, 400000000000000)}')
    print(f'Part 2: {solve_part2(input_lines)}')
