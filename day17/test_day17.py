import unittest

import day17 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "2413432311323",
            "3215453535623",
            "3255245654254",
            "3446585845452",
            "4546657867536",
            "1438598798454",
            "4457876987766",
            "3637877979653",
            "4654967986887",
            "4564679986453",
            "1224686865563",
            "2546548887735",
            "4322674655533"
        ]

    def test_solve_part1(self):
        self.assertEqual(102, day.solve_part1(self.lines))

    def test_solve_part2(self):
        self.assertEqual(94, day.solve_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
