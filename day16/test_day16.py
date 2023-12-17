import unittest

import day16 as day
from util.file import readfile


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = readfile("input.ex")

    def test_solve_part1(self):
        self.assertEqual(46, day.solve_part1(self.lines))

    def test_solve_part2(self):
        self.assertEqual(51, day.solve_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
