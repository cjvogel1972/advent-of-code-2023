import unittest

import day15 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = ["rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"]

    def test_solve_part1(self):
        self.assertEqual(1320, day.solve_part1(self.lines))

    def test_hash(self):
        self.assertEqual(52, day.hash_value("HASH"))

    def test_solve_part2(self):
        self.assertEqual(145, day.solve_part2(self.lines))


if __name__ == '__main__':
    unittest.main()
