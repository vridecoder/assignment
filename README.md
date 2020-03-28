# Partitioning problem

An arbitrary list of positive integers of any length and in any order
Determine if the list is partitionable or not. A partitioned list is one where it can be split into 2 sub-lists with equal sum. A sub-list can be any arbitrary (any set of numbers in any order) selection of numbers out of the parent list.


## Example:
Enumerate the list of cases to solve to minimize execution time

```bash
List = 1,2,3,4,5,6,7 = Partitionable 
List = 1,10,5,21,4 = Not Partitionable
List = 1,10,5,21,4,1 = Partitionable
```


## Code and Alogrithm
There are two main steps to solve this problem:

- Calculate sum of the array. If sum is odd, there can not be two subsets with equal sum, so return `false`.

- If sum of array elements is even, calculate `sum/2` and find a subset of array with sum equal to `sum/2`.

### Solution
  A class named `Partionable`, which exposes a method `checkSubset`, which is called recursively by itself, once invoked by `canPartion` method for the instance of `Partionable` class.
  Let `checkSubset(arr, n, sum/2)` be the function that returns true if 
        there is a subset of `arr[0..n-1]` with sum equal to `sum/2`

The problem can be divided into two subproblems
- `checkSubset()` without considering last element 
    `(reducing n to n-1)`
- `checkSubset` considering the last element 
    `(reducing sum/2 by arr[n-1] and n to n-1)`

If any of the above the above subproblems return `true`, then return `true`. 

```
self.checkSubset (arr, n, sum/2) = self.checkSubset (arr, n-1, sum/2) or
                            self.checkSubset (arr, n-1, sum/2 - arr[n-1])
```
```py

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
        if sum == 0:
            return True
        if n == 0 and sum != 0:
            return False
        # If last element is greater than sum, then
        # ignore it
        if arr[n-1] > sum:
            return self.checkSubset (arr, n-1, sum)

        # If not, see if sum can be obtained by including the last element
        # or excluding the last element

        return self.checkSubset (arr, n-1, sum) or self.checkSubset (arr, n-1, sum-arr[n-1])

```

### Time Complexity
 *O(2^n)* <br>
 In worst case, this solution tries two possibilities (whether to include or exclude) for every element.