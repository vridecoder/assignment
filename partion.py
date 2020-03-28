from functools import reduce


class Partionable:
    def __init__(self, numbers):
        self.data = numbers
        # Calculate sum of the elements in array
        self.sum = reduce(lambda a, b: a+b, numbers)
        self.length = len(numbers)

    # Returns true if self.data can be partitioned in two
    # subsets of equal sum, otherwise false
    def canPartion(self):
        # If self.sum is odd, there cannot be two subsets
        # with equal sum
        if self.sum % 2 != 0:
            return False

        # Find if there is subset with sum equal to
        # half of total sum
        return self.checkSubset(self.data, self.length, self.sum // 2)

    # Returns true if given array has subset of sum
    def checkSubset(self, arr, n, sum):
        pass


__all__ = ['Partionable']
