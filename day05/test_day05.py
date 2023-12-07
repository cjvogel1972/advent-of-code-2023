import unittest

import day05 as day
from util.file import readfile_blocks


class Test(unittest.TestCase):

    def test_solve_part1(self):
        self.assertEqual(35, day.solve_part1(readfile_blocks("input-ex.txt")))

    def test_solve_part2(self):
        self.assertEqual(46, day.solve_part2(readfile_blocks("input-ex.txt")))


if __name__ == '__main__':
    unittest.main()
