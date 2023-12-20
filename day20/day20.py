from collections import defaultdict
from math import lcm

from util.file import readfile

low, high = 0, 1


def solve_part1(lines: list[str]) -> int:
    modules = parse_modules(lines)

    low_count = 0
    high_count = 0
    for _ in range(1000):
        low_count += 1
        queue = [('broadcaster', '', low)]
        while queue:
            name, prev, pulse = queue.pop()

            module_type, destinations, state = modules[name]

            if name == 'broadcaster':
                low_count, high_count = add_pulse_counts(low_count, high_count, pulse, len(destinations))
                add_destinations(queue, modules, name, pulse, destinations)
            elif module_type == '%':
                if pulse == high:
                    continue

                new_pulse = high if not state else low

                low_count, high_count = add_pulse_counts(low_count, high_count, new_pulse, len(destinations))
                add_destinations(queue, modules, name, new_pulse, destinations)

                modules[name] = (module_type, destinations, not state)
            elif module_type == '&':
                state[prev] = pulse

                all_high = all([value == high for value in state.values()])
                new_pulse = low if all_high else high

                low_count, high_count = add_pulse_counts(low_count, high_count, new_pulse, len(destinations))
                add_destinations(queue, modules, name, new_pulse, destinations)

    return low_count * high_count


def add_pulse_counts(low_count, high_count, pulse, dest_count):
    if pulse == low:
        low_count += dest_count
    else:
        high_count += dest_count

    return low_count, high_count


def add_destinations(queue, modules, name, pulse, destinations):
    for destination in destinations:
        if destination in modules:
            queue.insert(0, (destination, name, pulse))


def solve_part2(lines: list[str]) -> int:
    modules = parse_modules(lines)

    counts = {}
    for prev in modules['gf'][2]:
        counts[prev] = 0

    button_pushes = 0
    done = False
    while not done:
        button_pushes += 1
        queue = [('broadcaster', '', low)]
        while queue:
            name, prev, pulse = queue.pop()

            module_type, destinations, state = modules[name]

            if name == 'broadcaster':
                add_destinations(queue, modules, name, pulse, destinations)
            elif module_type == '%':
                if pulse == high:
                    continue

                new_pulse = high if not state else low

                if name in counts and new_pulse == high and counts[name] == 0:
                    counts[name] = button_pushes

                add_destinations(queue, modules, name, new_pulse, destinations)
                modules[name] = (module_type, destinations, not state)
            elif module_type == '&':
                state[prev] = pulse

                all_high = all([value == high for value in state.values()])
                new_pulse = low if all_high else high

                if name in counts and new_pulse == high and counts[name] == 0:
                    counts[name] = button_pushes

                add_destinations(queue, modules, name, new_pulse, destinations)

        if all(x > 0 for x in counts.values()):
            done = True

    return lcm(*[x for x in counts.values()])


def parse_modules(lines):
    modules = {}
    for line in lines:
        module, destinations = line.split(" -> ")
        if module == "broadcaster":
            module_type = ""
            name = module
            data = ()
        else:
            module_type = module[0]
            name = module[1:]
            if module_type == "%":
                data = False
            else:
                data = {}

        modules[name] = (module_type, destinations.split(', '), data)

    for name, module in modules.items():
        module_type, _, state = module
        if module_type == '&':
            for name2, module2 in modules.items():
                other_destinations = module2[1]
                if name in other_destinations:
                    state[name2] = low

    return modules


if __name__ == '__main__':
    input_lines = readfile("day20/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
