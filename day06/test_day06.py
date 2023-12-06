import unittest

import day06 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "Time:      7  15   30",
            "Distance:  9  40  200"
        ]

    def test_solve_part1(self):
        self.assertEqual(288, day.solve_part1(self.lines))

    def test_solve_part2(self):
        self.assertEqual(71503, day.solve_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
