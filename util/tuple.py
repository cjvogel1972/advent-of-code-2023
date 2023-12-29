from operator import add


def tuple_add(t1, t2: tuple[int, int]) -> tuple:
    return tuple(map(add, t1, t2))
