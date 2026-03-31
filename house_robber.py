# https://leetcode.com/problems/house-robber/

import collections
from ast import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        t = [-1 for i in range(len(nums))]
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        t[0] = nums[0]
        t[1] = max(nums[0], nums[1])

        def rob_house(index):

            if index >= len(nums):
                return
            t[index] = max(t[index - 1], t[index - 2] + nums[index])
            rob_house(index + 1)

        rob_house(2)
        return t[len(nums) - 1]



