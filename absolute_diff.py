# https://leetcode.com/problems/minimum-absolute-difference-between-elements-with-constraint/description/

from sortedcontainers import SortedList
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        sorted_list = SortedList()
        min_diff = float('inf')

        for j in range(x, len(nums)):
            sorted_list.add(nums[j-x])

            target = nums[j]
            idx = sorted_list.bisect_left(target)
            if idx < len(sorted_list):
                min_diff = min(min_diff, sorted_list[idx] - target)

            if idx > 0:
                min_diff = min(min_diff, target - sorted_list[idx - 1])

        return min_diff