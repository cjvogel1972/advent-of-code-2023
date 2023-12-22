import unittest

import day22 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "1,0,1~1,2,1",
            "0,0,2~2,0,2",
            "0,2,3~2,2,3",
            "0,0,4~0,2,4",
            "2,0,5~2,2,5",
            "0,1,6~2,1,6",
            "1,1,8~1,1,9"
        ]

    def test_solve_part1(self):
        self.assertEqual(5, day.solve_part1(self.lines))

    def test_solve_part2(self):
        self.assertEqual(7, day.solve_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
