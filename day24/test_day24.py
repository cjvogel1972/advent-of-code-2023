import unittest

import day24 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "19, 13, 30 @ -2,  1, -2",
            "18, 19, 22 @ -1, -1, -2",
            "20, 25, 34 @ -2, -2, -4",
            "12, 31, 28 @ -1, -2, -1",
            "20, 19, 15 @  1, -5, -3"
        ]

    def test_solve_part1(self):
        self.assertEqual(2, day.solve_part1(self.lines, 7, 27))

    def test_solve_part2(self):
        self.assertEqual(0, day.solve_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
