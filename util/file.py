def readfile(filename: str) -> list[str]:
    """Return lines from file as a list, stripping off outer whitespace and newline characters"""
    with open(filename) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines
