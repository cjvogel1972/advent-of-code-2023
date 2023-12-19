import unittest

import day14 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "O....#....",
            "O.OO#....#",
            ".....##...",
            "OO.#O....O",
            ".O.....O#.",
            "O.#..O.#.#",
            "..O..#O..O",
            ".......O..",
            "#....###..",
            "#OO..#...."
        ]

    def test_solve_part1(self):
        self.assertEqual(136, day.solve_part1(self.lines))

    def test_solve_part2(self):
        self.assertEqual(64, day.solve_part2(self.lines))

    def test_cycle(self):
        grid = [list(line) for line in self.lines]
        expected = ".....#........#...O#...OO##....OO#...........OOO#..O#...O#.#....O#..........OOOO#...O###..#..OO#...."
        day.cycle(grid)
        self.assertEqual(expected, day.platform_to_string(grid))


if __name__ == '__main__':
    unittest.main()
