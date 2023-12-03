import unittest

import day03 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "467..114..",
            "...*......",
            "..35..633.",
            "......#...",
            "617*......",
            ".....+.58.",
            "..592.....",
            "......755.",
            "...$.*....",
            ".664.598.."
        ]

    def test_solve_part1(self):
        self.assertEqual(4361, day.solve_part1(self.lines))

    def test_solve_part1_alt(self):
        self.assertEqual(4361, day.solve_part1_alt(self.lines))

    def test_solve_part2(self):
        self.assertEqual(467835, day.solve_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
