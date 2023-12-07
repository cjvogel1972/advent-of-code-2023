def readfile(filename: str) -> list[str]:
    """Return lines from file as a list, stripping off outer whitespace and newline characters"""
    with open(filename) as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return lines


def readfile_blocks(filename: str) -> list[str]:
    """Return blocks of data from the file as a list, based on there being blank lines separating the blocks"""
    with open(filename) as f:
        blocks = f.read().split("\n\n")

    return blocks
