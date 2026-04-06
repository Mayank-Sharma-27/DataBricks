# https://www.hack2hire.com/companies/databricks/coding-questions/68560fd24d16ce2ead6e1758/practice?questionId=685637ce4d16ce2ead6e1769


from collections import defaultdict
from types import new_class


class Solution:
    def encode(self, values):
        if values is None or len(values) == 0:
            return []
        ans = []

        i = 0

        while i < len(values):
            run_start = i
            value = values[i]
            count = 1

            while i + 1 < len(values) and values[i + 1] == value:
                i += 1
                count += 1

            if count >= 8 or (i == len(values) - 1 and count > 1):
                ans.append(f"RLE[{value}, {count}]]")
                i += 1
            else:
                start = run_start
                end = min(start + 8, len(values))
                bp = "BP["
                for j in range(start, end):

                    if j > start:
                        bp += ","
                    bp += str(values[j])
                bp += "]"

                ans.append(bp)
                i = end
        return ans

    def decode(self, runs):
        ans = []
        for run in runs:
            type = run.split("[")[0]
            if type == "RLE":
                number = run.split(",")[0].split("[")[1].strip()
                count = int(run.split(",")[1].split("]")[0].strip())
                for i in range(count):
                    ans.append(int(number))
            else:
                array_start = run.split("BP[")[1]

                array = array_start.split("]")[0]

                numbers = array.split(",")
                for n in numbers:
                    n = n.strip()
                    ans.append(int(n))

        return ans


def test1():
    print("======== test 1: =========")
    solution = Solution()

    input = [5, 5, 5, 5, 5, 5, 5, 5, 1, 2, 3]
    encoded = solution.encode(input)
    print("encoded: " + str(encoded))
    # Expected: ["RLE[5,8]", "BP[1,2,3]"]

    decoded = solution.decode(encoded)
    print("decoded: " + str(decoded))
    # Expected: [5, 5, 5, 5, 5, 5, 5, 5, 1, 2, 3]


def test2():
    print("\n======== test 2: =========")
    solution = Solution()

    input = [1, 1, 1]
    encoded = solution.encode(input)
    print("encoded: " + str(encoded))
    # Expected: ["RLE[1,3]"]

    decoded = solution.decode(encoded)
    print("decoded: " + str(decoded))
    # Expected: [1, 1, 1]


def test3():
    print("\n======== test 3: =========")
    solution = Solution()

    input = [1, 1, 1, 1, 2, 3, 4, 5]
    encoded = solution.encode(input)
    print("encoded: " + str(encoded))
    # Expected: ["BP[1,1,1,1,2,3,4,5]"]

    decoded = solution.decode(encoded)
    print("decoded: " + str(decoded))
    # Expected: [1, 1, 1, 1, 2, 3, 4, 5]


def test4():
    print("\n======== test 4: =========")
    solution = Solution()

    input = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    encoded = solution.encode(input)
    print("encoded: " + str(encoded))
    # Expected: ["BP[1,1,1,1,2,3,4,5]", "BP[6,7,8,9,10,11,12,13]"]

    decoded = solution.decode(encoded)
    print("decoded: " + str(decoded))
    # Expected: [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def test5():
    print("\n======== test 5: =========")
    solution = Solution()

    input = [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 10, 11]
    encoded = solution.encode(input)
    print("encoded: " + str(encoded))
    # Expected: ["RLE[0,8]", "BP[1,2,3,4,5,6,7,8]", "RLE[9,10]", "BP[10,11]"]

    decoded = solution.decode(encoded)
    print("decoded: " + str(decoded))
    # Expected: [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9,
    # 9, 9, 9, 9, 10, 11]


def test6():
    print("\n======== test 6: =========")
    solution = Solution()

    input = [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]
    encoded = solution.encode(input)
    print("encoded: " + str(encoded))
    # Expected: ["RLE[0,8]", "BP[1,2,3,4,5,6,7,8]", "RLE[9,3]"]

    decoded = solution.decode(encoded)
    print("decoded: " + str(decoded))
    # Expected: [0, 0, 0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9]


if __name__ == "__main__":
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()