#https://www.hack2hire.com/companies/databricks/coding-questions/68521e291af0034b322764c7/practice?questionId=68523a801af0034b322764d9


from typing import List, Optional
from collections import deque


class Solution:
    def findOptimalCommute(self, grid: List[List[str]], modes: List[str], costs: List[int], times: List[int]) -> str:
        cost_by_mode = []
        dx = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def calculate_cost(row, col, mode, cost, time):

            total_cost = 0
            total_time = 0
            visited = [[False for j in range(len(grid))] for i in range(len(grid[0]))]
            queue = deque()
            queue.append([row, col, total_cost, total_time])
            visited[row][col] = True

            while queue:
                size = len(queue)

                for i in range(size):
                    curr_x, curr_y, curr_cost, curr_time = queue.popleft()

                    visited[curr_x][curr_y] = True
                    for d in dx:
                        x = d[0] + curr_x
                        y = d[1] + curr_y
                        if x < 0 or y < 0 or x >= len(grid) or y >= len(grid):
                            continue
                        if grid[x][y] == "D":
                            return curr_cost, curr_time
                        if grid[x][y] != str(mode) or visited[x][y] or grid[x][y] == "X":
                            continue

                        queue.append([x, y, curr_cost + cost, curr_time + time])
                        # print(queue)

            return float('inf'), float('inf')

        min_time = float('inf')
        ans = ""
        min_cost = float('inf')
        for k in range(len(modes)):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == "S":
                        # print(costs[k])
                        total_cost, total_time = calculate_cost(i, j, k + 1, costs[k], times[k])
                        # print(total_time)
                        if min_time > total_time:
                            min_time = total_time
                            min_cost = total_cost
                            ans = modes[k]
                            # print(ans)
                        elif min_time == total_time:
                            min_time = total_time
                            if min_cost > total_cost:
                                min_cost = total_cost
                                ans = modes[k]

        return ans



