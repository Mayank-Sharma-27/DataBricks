# https://www.hack2hire.com/companies/databricks/coding-questions/68539976d3dbd4fb8b026e9e/practice?questionId=68539b6bd3dbd4fb8b026e9f

from collections import deque
class LazyArray:
    def __init__(self, arr, function= None):
        if not function:
            self.arr = arr
            self.functions = []
        else:
            self.arr =  arr.copy()
            self.functions = function.copy()

    def map(self, fn):
        newArray = LazyArray(self.arr, self.functions)
        newArray.functions.append(fn)
        return newArray

    def indexOf(self, target):
        for i in range(len(self.arr)):
            value = self.arr[i]
            for fn in self.functions:
                value = fn(value)
            if value == target:
                return i
        return -1


if __name__ == "__main__":
    # Test case 1
    arr1 = LazyArray([10, 20, 30, 40, 50])
    print(arr1.map(lambda n: n * 2).indexOf(40))  # Expected: 1

    # Test case 2
    arr2 = LazyArray([10, 20, 30, 40, 50])
    print(arr2.map(lambda n: n * 2).map(lambda n: n * 3).indexOf(240))  # Expected: 3

    # Test case 3
    arr3 = LazyArray([1, 2, 3, 4, 5])
    print(arr3.map(lambda n: n + 10).indexOf(100))  # Expected: -1

    # Test case 4
    arr4 = LazyArray([5, 10, 15, 20, 25])
    print(arr4.map(lambda n: n * 2).map(lambda n: n + 5).map(lambda n: n // 3).indexOf(11))  # Expected: 2

    # Test case 5
    arr5 = LazyArray([-5, 1, 2, -1, 10])
    print(arr5.map(lambda n: n * 3).map(lambda n: n + 4).map(lambda n: n - 2).indexOf(8))  # Expected: 2