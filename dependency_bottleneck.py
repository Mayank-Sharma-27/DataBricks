#https://www.hack2hire.com/companies/databricks/coding-questions/684b54b44023c4f502877db8/practice?questionId=684ba2bf4023c4f502877de9

from typing import List, Optional
from collections import deque


class Solution:
    def findBottlenecks(self, n: int, edges: List[List[int]]) -> List[int]:
        if not n:
            return []
        dependencies = [0 for i in range(n)]
        for edge in edges:
            u, v = edge
            dependencies[v] += 1
        queue = deque()

        for i in range(n):
            if dependencies[i] == 0:
                queue.append(i)
        bottlenecks = []
        if not queue:
            return []
        completed_dependencies = 0
        completed_set = set()
        while queue:
            size = len(queue)

            for i in range(size):
                dep = queue.popleft()

                if size == 1:
                    bottlenecks.append(dep)
                for edge in edges:
                    if edge[0] == dep:
                        dependencies[edge[1]] -= 1
                        if dependencies[edge[1]] == 0:
                            queue.append(edge[1])
        return bottlenecks






 