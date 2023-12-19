def manhattan_distance(loc1: tuple[int, int], loc2: tuple[int, int]) -> int:
    """Compute the Manhattan distance between two coordinates"""
    return abs(loc1[0] - loc2[0]) + abs(loc1[1] - loc2[1])