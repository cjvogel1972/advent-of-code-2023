import unittest

import day08 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "RL",
            "",
            "AAA = (BBB, CCC)",
            "BBB = (DDD, EEE)",
            "CCC = (ZZZ, GGG)",
            "DDD = (DDD, DDD)",
            "EEE = (EEE, EEE)",
            "GGG = (GGG, GGG)",
            "ZZZ = (ZZZ, ZZZ)"
        ]

    def test_solve_part1(self):
        self.assertEqual(2, day.solve_part1(self.lines))

    def test_solve_part1_repeat_direction(self):
        lines = [
            "LLR",
            "",
            "AAA = (BBB, BBB)",
            "BBB = (AAA, ZZZ)",
            "ZZZ = (ZZZ, ZZZ)"
        ]
        self.assertEqual(6, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "LR",
            "",
            "11A = (11B, XXX)",
            "11B = (XXX, 11Z)",
            "11Z = (11B, XXX)",
            "22A = (22B, XXX)",
            "22B = (22C, 22C)",
            "22C = (22Z, 22Z)",
            "22Z = (22B, 22B)",
            "XXX = (XXX, XXX)"
        ]
        self.assertEqual(6, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
