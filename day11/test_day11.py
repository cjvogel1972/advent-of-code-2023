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
        self.assertEqual(374, day.solve_part1(self.lines))

    def test_solve_part2(self):
        self.assertEqual(8410, day.solve_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
