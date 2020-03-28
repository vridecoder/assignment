import unittest
from partion import Partionable
class TestPartionableMethods(unittest.TestCase):

    def test_data(self):
        arr = [1,2,3,4,5,6,7]
        partion = Partionable(arr)
        self.assertEqual(partion.data, arr)

    def test_checkPartionMethod(self):
        arr = [1,2,3,4,5,6,7]
        partion = Partionable(arr)
        self.assertEqual(partion.canPartion(), True)

    def test_checkSubsetMethod(self):
        arr = [1,2,3,4,5,6,7]
        partion = Partionable(arr)
        self.assertEqual(partion.checkSubset(arr, len(arr), sum(arr) ), True)


if __name__ == '__main__':
    unittest.main()