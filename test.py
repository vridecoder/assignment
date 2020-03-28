import unittest
from partion import Partionable
class TestPartionableMethods(unittest.TestCase):

    def test_data(self):
        arr = [1,2,3,4,5,6,7]
        partion = Partionable(arr)
        self.assertEqual(partion.data, arr)

    def test_checkPartionIsMethod(self):
        arr = [1,2,3,4,5,6,7]
        partion = Partionable(arr)
        self.assertEqual(partion.canPartion(), True)


if __name__ == '__main__':
    unittest.main()