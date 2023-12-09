import unittest

import day09 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "0 3 6 9 12 15",
            "1 3 6 10 15 21",
            "10 13 16 21 30 45"
        ]

    def test_solve_part1(self):
        self.assertEqual(114, day.solve_part1(self.lines))

    def test_solve_part2(self):
        self.assertEqual(2, day.solve_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
