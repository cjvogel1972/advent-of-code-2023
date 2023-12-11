from util.file import readfile


def solve_part1(lines: list[str]) -> int:
    total = 0

    skip_next = False
    for r, row in enumerate(lines):
        if skip_next:
            skip_next = False
            continue
        if row.count('.') == len(row):
            lines.insert(r, row)
            skip_next = True

    cols = zip(*lines)
    col_inserted = 0
    for c, col in enumerate(cols):
        if col.count('.') == len(col):
            for i, line in enumerate(lines):
                lines[i] = line[:c + col_inserted] + '.' + line[c + col_inserted:]
            col_inserted += 1

    for r, row in enumerate(lines):
        start_loc = 0
        while row.count('#', start_loc) > 0:
            c = row.index("#", start_loc)
            start_loc = c + 1

            next_start_loc = c + 1
            while row.count("#", next_start_loc) > 0:
                c1 = row.index("#", next_start_loc)
                next_start_loc = c1 + 1
                total += (c1 - c)

            for r1 in range(r + 1, len(lines)):
                row1 = lines[r1]
                next_start_loc = 0
                while row1.count("#", next_start_loc) > 0:
                    c1 = row1.index("#", next_start_loc)
                    next_start_loc = c1 + 1
                    total += abs(r1 - r) + abs(c1 - c)

    return total


def solve_part2(lines: list[str]) -> int:
    expansion = 1000000
    total = 0

    expansion_str = '.' * expansion
    cols = zip(*lines)
    col_inserted = 0
    for c, col in enumerate(cols):
        if col.count('.') == len(col):
            for i, line in enumerate(lines):
                lines[i] = line[:c + col_inserted] + expansion_str + line[c + 1 + col_inserted:]
            col_inserted += expansion - 1

    empty_rows = []
    for r, row in enumerate(lines):
        if row.count('.') == len(row):
            empty_rows.append(r)

    expansion_lines = [lines[empty_rows[0]]] * expansion
    for i in reversed(empty_rows):
        lines[i:i + 1] = expansion_lines

    r = 0
    while r < len(lines):
        print(r)
        row = lines[r]
        if row.count('.') == len(row):
            r += expansion
            continue
        start_loc = 0
        while row.count('#', start_loc) > 0:
            c = row.index("#", start_loc)
            start_loc = c + 1

            next_start_loc = c + 1
            while row.count("#", next_start_loc) > 0:
                c1 = row.index("#", next_start_loc)
                next_start_loc = c1 + 1
                total += (c1 - c)

            r1 = r + 1
            while r1 < len(lines):
                row1 = lines[r1]
                if row1.count('.') == len(row1):
                    r1 += expansion
                    # print(r1)
                    continue
                next_start_loc = 0
                while row1.count("#", next_start_loc) > 0:
                    c1 = row1.index("#", next_start_loc)
                    next_start_loc = c1 + 1
                    total += abs(r1 - r) + abs(c1 - c)
                r1 += 1
        r += 1

    return total


if __name__ == '__main__':
    input_lines = readfile("day11/input.txt")
    print(f'Part 1: {solve_part1(input_lines)}')

    input_lines = readfile("day11/input.txt")
    print(f'Part 2: {solve_part2(input_lines)}')
