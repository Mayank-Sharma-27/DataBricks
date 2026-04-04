from typing import List, Optional
# https://www.hack2hire.com/companies/databricks/coding-questions/685303ac1af0034b3227652d/practice?questionId=685303fe1af0034b3227652e
class Solution:
    def findPath(self, order: int, source: int, dest: int) -> str:
        size = [1] * (order +1)
        for n in range(2, order +1):
            size[n] = 1+ size[n-2] + size[n-1]

        def get_path(n, start, target):
            if start == target:
                return ""

            left_start = start +1
            left_end = start + size[n-2]
            right_start = start + size[n-2] + 1

            if left_start <= target <= left_end:
                return "L" + get_path(n-2, left_start, target)
            else:
                return "R" + get_path(n-1, right_start, target)
        path_src = get_path(order, 0, source)
        path_dst = get_path(order, 0, dest)

        i =0
        while i < len(path_src) and i < len(path_dst) and path_src[i] == path_dst[i]:
            i+=1
        return "U"* (len(path_src) -i) + path_dst[i:]
