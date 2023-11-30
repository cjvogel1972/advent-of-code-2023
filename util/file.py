def readfile(filename: str) -> list[str]:
    with open(filename) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines
