import unittest

import day20 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "broadcaster -> a, b, c",
            "%a -> b",
            "%b -> c",
            "%c -> inv",
            "&inv -> a"
        ]

    def test_solve_part1(self):
        self.assertEqual(32000000, day.solve_part1(self.lines))

    def test_solve_part1_alt(self):
        lines = [
            "broadcaster -> a",
            "%a -> inv, con",
            "&inv -> b",
            "%b -> con",
            "&con -> output"
        ]
        self.assertEqual(11687500, day.solve_part1(lines))


if __name__ == '__main__':
    unittest.main()
