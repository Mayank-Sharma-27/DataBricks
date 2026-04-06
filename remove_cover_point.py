# https://www.hack2hire.com/companies/databricks/coding-questions/684db91acab8e9bb7ea93b44/practice?questionId=684dee4b5e4cf21833c0611f
# "I have two approaches. The first flattens all intervals into actual points — it's correct but completely infeasible given intervals can go up to 10⁹. That's potentially billions of numbers in memory.
# The second approach never expands the intervals at all. It treats each interval as a count of points, walks through intervals accumulating that count, and finds the target mathematically. Once found, it handles four simple cases — shrink left, shrink right, split, or eliminate. That's O(N) time and O(1) extra space.
# Solution 2 is clearly the right answer."


from typing import List, Optional

class Solution:
    def deleteCoveredPoint(self, intervals: List[List[int]], idx: int) -> List[List[int]]:

        count =0
        target_idx = -1
        target_value = -1

        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            length = end - start
            if idx < count + length:
                target_idx = i
                target_value = start + (idx - count)
                break
            count += length

        res = []
        for i in range(len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]

            if i != target_idx:
                res.append([s,e])
            else:
                if s + 1 == e and s == target_value:
                    continue
                elif target_value == s:
                    res.append([s+1, e])
                elif e -1 == target_value:
                    res.append([s, e-1])
                else:
                    res.append([s, target_value])
                    res.append([target_value +1, e])
        return res






