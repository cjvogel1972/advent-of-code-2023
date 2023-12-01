import unittest

import day01 as day


class Test(unittest.TestCase):

    def test_solve_part1(self):
        lines = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet"
        ]

        self.assertEqual(142, day.solve_part1(lines))

    def test_solve_part2(self):
        lines = [
            "two1nine",
            "eightwothree",
            "abcone2threexyz",
            "xtwone3four",
            "4nineeightseven2",
            "zoneight234",
            "7pqrstsixteen"
        ]

        self.assertEqual(281, day.solve_part2(lines))


if __name__ == '__main__':
    unittest.main()
