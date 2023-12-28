import unittest

import day23.day23 as day
from util.file import readfile


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = readfile("day23/input.ex")

    def test_solve_part1(self):
        self.assertEqual(94, day.solve_part1(self.lines))

    def test_solve_part2(self):
        self.assertEqual(0, day.solve_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
