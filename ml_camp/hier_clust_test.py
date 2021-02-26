# basic tesing file for Hierarchical Clustering 

from hier_clust import *
import unittest
class TestMe(unittest.TestCase):
    def setUp(self) -> None:
        self.t = Hier()
        print(self.t)
    @unittest.skip('skipping str')
    def test_1(self):
        print(str(self.t))
    def test_3(self):
        self.t.pre()
        print(self.t.shape)

if __name__ == "__main__":
    unittest.main()