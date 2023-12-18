from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    current = (0, 0)
    boundary_points = 0
    vertices = [current]
    for line in lines:
        direction, distance, _ = line.split()
        distance = int(distance)
        if direction == "R":
            delta = (0, distance)
        elif direction == "D":
            delta = (distance, 0)
        elif direction == "L":
            delta = (0, -distance)
        else:
            delta = (-distance, 0)

        current = (current[0] + delta[0], current[1] + delta[1])
        vertices.append(current)
        boundary_points += distance

    return compute_area(vertices, boundary_points)


def compute_area(vertices: list[tuple], boundary_points: int) -> int:
    # use shoelace formula
    area = 0.0
    points = zip(vertices, vertices[1:])
    for p1, p2 in points:
        area += (p2[0] - p1[0]) * (p2[1] + p1[1])

    area = int(abs(area / 2.0))

    # use Pick's theorem to find the internal area
    interior_area = area - (boundary_points // 2) + 1

    # re-add the boundary points for the total area
    return interior_area + boundary_points


def solve_part2(lines: list[str]) -> int:
    current = (0, 0)
    boundary_points = 0
    vertices = [current]
    for line in lines:
        _, _, color = line.split()
        distance = color[2:-2]
        direction = color[-2]
        distance = int(distance, 16)
        if direction == "0":
            delta = (0, distance)
        elif direction == "1":
            delta = (distance, 0)
        elif direction == "2":
            delta = (0, -distance)
        else:
            delta = (-distance, 0)

        current = (current[0] + delta[0], current[1] + delta[1])
        vertices.append(current)
        boundary_points += distance

    return compute_area(vertices, boundary_points)


if __name__ == '__main__':
    input_lines = readfile("day18/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
