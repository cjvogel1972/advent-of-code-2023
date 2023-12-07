import unittest

import day07 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "32T3K 765",
            "T55J5 684",
            "KK677 28",
            "KTJJT 220",
            "QQQJA 483"
        ]

    def test_solve_part1(self):
        self.assertEqual(6440, day.solve_part1(self.lines))

    def test_solve_part2(self):
        self.assertEqual(5905, day.solve_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
