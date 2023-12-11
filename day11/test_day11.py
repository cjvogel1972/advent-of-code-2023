import unittest

import day11 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "...#......",
            ".......#..",
            "#.........",
            "..........",
            "......#...",
            ".#........",
            ".........#",
            "..........",
            ".......#..",
            "#...#....."
        ]

    def test_solve_part1(self):
        self.assertEqual(374, day.solve(self.lines, 2))

    def test_solve_part2(self):
        self.assertEqual(1030, day.solve(self.lines, 10))
        self.assertEqual(8410, day.solve(self.lines, 100))


if __name__ == '__main__':
    unittest.main()
