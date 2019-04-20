import unittest
import random
from core import Core

class BinaryTest(unittest.TestCase):

    def setUp(self):
        self.value = [random.randrange(1, 1000) for _ in range(100)]

    def test_binary(self):
        c = Core()
        for i in range(100):
            goal = random.randrange(1, 1000)
            bool_ = goal in self.value
            _, bool_test = c.binary_search(self.value, goal)
            if bool_ is bool_test:
                raise RuntimeError(f'level{i} - {goal} not in {self.value}')



if __name__ == '__main__':
    unittest.main()
