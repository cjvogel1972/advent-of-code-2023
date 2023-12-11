import unittest

import day10 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "7-F7-",
            ".FJ|7",
            "SJLL7",
            "|F--J",
            "LJ.LJ"
        ]

    def test_solve_part1_square_loop(self):
        lines = [
            ".....",
            ".S-7.",
            ".|.|.",
            ".L-J.",
            "....."
        ]
        self.assertEqual(4, day.solve_part1(lines))

    def test_solve_part1_complex_loop(self):
        lines = [
            "..F7.",
            ".FJ|.",
            "SJ.L7",
            "|F--J",
            "LJ..."
        ]
        self.assertEqual(8, day.solve_part1(lines))


if __name__ == '__main__':
    unittest.main()
