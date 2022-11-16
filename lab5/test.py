import unittest
import time
from lab5.main import do_rabin_karp


class TestDoRabinKarp(unittest.TestCase):
    def setUp(self) -> None:
        self.text1 = "abababababab"
        self.pattern1 = "ab"
        self.match_idx1 = [0, 2, 4, 6, 8, 10]

        self.text2 = "viruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslvivviruslviv"
        self.pattern2 = "russian"
        self.match_idx2 = []

        self.text3 = "Ya"
        self.pattern3 = "Ya"
        self.match_idx3 = [0]

        self.text4 = "CRINGEBASEDCRINGEBASED"
        self.pattern4 = "BASED"
        self.match_idx4 = [6, 17]

    def test1(self):
        st = time.time()
        pattern_idx = do_rabin_karp(self.pattern1, self.text1)
        end = time.time()
        print(end - st)
        self.assertEqual(pattern_idx, self.match_idx1)

    def test2(self):
        st = time.time()
        pattern_idx = do_rabin_karp(self.pattern2, self.text2)
        end = time.time()
        print(end - st)
        self.assertEqual(pattern_idx, self.match_idx2)

    def test3(self):
        st = time.time()
        pattern_idx = do_rabin_karp(self.pattern3, self.text3)
        end = time.time()
        print(end - st)
        self.assertEqual(pattern_idx, self.match_idx3)

    def test4(self):
        st = time.time()
        pattern_idx = do_rabin_karp(self.pattern4, self.text4)
        end = time.time()
        print(end - st)
        self.assertEqual(pattern_idx, self.match_idx4)


if __name__ == '__main__':
    unittest.main()
