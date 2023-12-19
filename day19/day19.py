from copy import deepcopy

from util.file import readfile_blocks


def solve_part1(blocks: list[str]) -> int:
    wf, ratings = blocks

    workflows = parse_workflows(wf)

    total = 0

    for rating in ratings.strip().split('\n'):
        x, m, a, s = [int(v.split('=')[1]) for v in rating[1:-1].split(',')]
        current_workflow = 'in'
        while current_workflow not in 'AR':
            prev_workflow = current_workflow
            rules = workflows[current_workflow]
            for rule in rules:
                var_name, op, value, action = parse_rule(rule)
                if op != '':
                    if var_name == 'x':
                        if op == '<':
                            if x < value:
                                current_workflow = action
                        else:
                            if x > value:
                                current_workflow = action
                    elif var_name == 'm':
                        if op == '<':
                            if m < value:
                                current_workflow = action
                        else:
                            if m > value:
                                current_workflow = action
                    elif var_name == 'a':
                        if op == '<':
                            if a < value:
                                current_workflow = action
                        else:
                            if a > value:
                                current_workflow = action
                    elif var_name == 's':
                        if op == '<':
                            if s < value:
                                current_workflow = action
                        else:
                            if s > value:
                                current_workflow = action
                else:
                    current_workflow = action

                if current_workflow == 'A':
                    total += x + m + a + s
                    break
                elif current_workflow != prev_workflow:
                    break

    return total


def parse_rule(rule: str) -> tuple[str, str, int, str]:
    if ':' in rule:
        condition, action = rule.split(':')
        var_name = condition[0]
        op = condition[1]
        value = int(condition[2:])
    else:
        var_name = ''
        op = ''
        value = 0
        action = rule

    return var_name, op, value, action


def parse_workflows(wf: str) -> dict[str, list[str]]:
    workflows = {}

    for w in wf.strip().split('\n'):
        name, rules = w.split('{')
        rules = rules[:-1]
        rules = rules.split(',')
        workflows[name] = rules

    return workflows


def solve_part2(blocks: list[str]) -> int:
    total = 0

    wf, _ = blocks

    workflows = parse_workflows(wf)

    paths = []
    follow_paths(paths, workflows, ["in"], "in")

    for path in paths:
        x = (1, 4000)
        m = (1, 4000)
        a = (1, 4000)
        s = (1, 4000)

        nodes = path.split(',')
        for i, node in enumerate(nodes[:-1]):
            next_node = nodes[i + 1]
            rules = [parse_rule(rule) for rule in workflows[node]]
            accept_count = 0
            for rule in rules:
                var_name = rule[0]
                action = rule[3]
                if action == 'A':
                    accept_count += 1
                    action = action + str(accept_count)
                    rule = (*rule[:3], action)

                if var_name == 'x':
                    x = compute_new_range(rule, x, next_node)
                elif var_name == 'm':
                    m = compute_new_range(rule, m, next_node)
                elif var_name == 'a':
                    a = compute_new_range(rule, a, next_node)
                elif var_name == 's':
                    s = compute_new_range(rule, s, next_node)

                if action == next_node:
                    break

        total += ((x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1))

    return total


def compute_new_range(rule, old_range, next_node):
    var_name, op, value, action = rule

    new_range = old_range
    if next_node == action:
        if op == '<':
            if old_range[0] < value < old_range[1]:
                new_range = (old_range[0], value - 1)
        else:
            if old_range[1] > value > old_range[0]:
                new_range = (value + 1, old_range[1])
    else:
        if op == '<':
            if old_range[0] < value < old_range[1]:
                new_range = (value, old_range[1])
        else:
            if old_range[1] > value > old_range[0]:
                new_range = (old_range[0], value)

    return new_range


def follow_paths(paths, workflows, path, current_node):
    rules = workflows[current_node]
    accept_count = 0
    for rule in rules:
        _, _, _, action = parse_rule(rule)
        if action == 'A':
            accept_count += 1
            new_path = deepcopy(path)
            new_path.append(action + str(accept_count))
            paths.append(",".join(new_path))
        elif action != 'R':
            new_path = deepcopy(path)
            new_path.append(action)
            follow_paths(paths, workflows, new_path, action)


if __name__ == '__main__':
    input_lines = readfile_blocks("day19/input.txt")

    print(f'Part 1: {solve_part1(input_lines)}')
    print(f'Part 2: {solve_part2(input_lines)}')
