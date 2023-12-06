from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 1

    races_times = list(map(int, lines[0].split(":")[1].split()))
    races_distances = list(map(int, lines[1].split(":")[1].split()))

    for i, race_time in enumerate(races_times):
        race_distance = races_distances[i]

        total *= compute_record_setting_races(race_time, race_distance)

    return total


def solve_part2(lines: list[str]) -> int:
    race_time = int("".join(lines[0].split(":")[1].split()))
    race_distance = int("".join(lines[1].split(":")[1].split()))

    return compute_record_setting_races(race_time, race_distance)


def compute_record_setting_races(race_time: int, race_distance: int) -> int:
    beat_record = 0

    for button_push_time in range(race_time + 1):
        speed = button_push_time
        run_time = race_time - speed
        distance = speed * run_time

        beat_record += 1 if distance > race_distance else 0

    return beat_record


if __name__ == '__main__':
    input_lines = readfile("day06/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
