import unittest

import day13 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.blocks = [
            "#.##..##.\n" +
            "..#.##.#.\n" +
            "##......#\n" +
            "##......#\n" +
            "..#.##.#.\n" +
            "..##..##.\n" +
            "#.#.##.#.\n",
            "#...##..#\n" +
            "#....#..#\n" +
            "..##..###\n" +
            "#####.##.\n" +
            "#####.##.\n" +
            "..##..###\n" +
            "#....#..#\n"
        ]

    def test_solve_part1(self):
        self.assertEqual(405, day.solve_part1(self.blocks))

    def test_solve_part2(self):
        self.assertEqual(400, day.solve_part2(self.blocks))


if __name__ == '__main__':
    unittest.main()
