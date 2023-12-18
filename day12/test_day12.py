import unittest

import day12 as day


class Test(unittest.TestCase):

    def setUp(self):
        self.lines = [
            "???.### 1,1,3",
            ".??..??...?##. 1,1,3",
            "?#?#?#?#?#?#?#? 1,3,1,6",
            "????.#...#... 4,1,1",
            "????.######..#####. 1,6,5",
            "?###???????? 3,2,1"
        ]

    def test_solve_part1(self):
        self.assertEqual(21, day.solve_part1(self.lines))

    def test_part1_count_possibilities_1(self):
        self.assertEqual(1, day.count_possibilities("???.###", [1, 1, 3]))

    def test_part1_count_possibilities_2(self):
        self.assertEqual(4, day.count_possibilities(".??..??...?##.", [1, 1, 3]))

    def test_part1_count_possibilities_3(self):
        self.assertEqual(1, day.count_possibilities("?#?#?#?#?#?#?#?", [1, 3, 1, 6]))

    def test_part1_count_possibilities_4(self):
        self.assertEqual(1, day.count_possibilities("????.#...#...", [4, 1, 1]))

    def test_part1_count_possibilities_5(self):
        self.assertEqual(4, day.count_possibilities("????.######..#####.", [1, 6, 5]))

    def test_part1_count_possibilities_6(self):
        self.assertEqual(10, day.count_possibilities("?###????????", [3, 2, 1]))

    def test_solve_part2(self):
        self.assertEqual(525152, day.solve_part2(self.lines))

    def test_part2_unfold(self):
        springs, records = day.unfold("???.###", [1, 1, 3])
        self.assertEqual("???.###????.###????.###????.###????.###", springs)
        self.assertEqual([1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3], records)

    def test_part2_unfold_and_count_possibilities_1(self):
        self.assertEqual(1, day.unfold_and_count_possibilities("???.###", [1, 1, 3]))

    def test_part2_unfold_and_count_possibilities_2(self):
        self.assertEqual(16384, day.unfold_and_count_possibilities(".??..??...?##.", [1, 1, 3]))

    def test_part2_unfold_and_count_possibilities_3(self):
        self.assertEqual(1, day.unfold_and_count_possibilities("?#?#?#?#?#?#?#?", [1, 3, 1, 6]))

    def test_part2_unfold_and_count_possibilities_4(self):
        self.assertEqual(16, day.unfold_and_count_possibilities("????.#...#...", [4, 1, 1]))

    def test_part2_unfold_and_count_possibilities_5(self):
        self.assertEqual(2500, day.unfold_and_count_possibilities("????.######..#####.", [1, 6, 5]))

    def test_part2_unfold_and_count_possibilities_6(self):
        self.assertEqual(506250, day.unfold_and_count_possibilities("?###????????", [3, 2, 1]))


if __name__ == '__main__':
    unittest.main()
