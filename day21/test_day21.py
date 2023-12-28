import unittest

import day21 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "...........",
            ".....###.#.",
            ".###.##..#.",
            "..#.#...#..",
            "....#.#....",
            ".##..S####.",
            ".##..#...#.",
            ".......##..",
            ".##.#.####.",
            ".##..##.##.",
            "..........."
        ]

    def test_solve_part1(self):
        self.assertEqual(16, day.solve_part1(self.lines, 6))

    def test_solve_part2(self):
        self.assertEqual(0, day.solve_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
