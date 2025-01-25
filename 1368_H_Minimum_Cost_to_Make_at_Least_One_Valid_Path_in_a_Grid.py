import heapq
from typing import List


def minCost(grid: List[List[int]]) -> int:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    num_row, num_col = len(grid), len(grid[0])
    min_heap = [(0, 0, 0)]
    min_cost = [[float("inf")] * (num_col) for _ in range(num_row)]
    min_cost[0][0] = 0
    while min_heap:
        cost, row, col = heapq.heappop(min_heap)
        if min_cost[row][col] != cost:
            continue
        for n, (r, c) in enumerate(directions):
            r2, c2 = (row+r), (col+c)
            if r2 < 0 or r2 >= num_row or c2 < 0 or c2 >= num_col:
                continue
            new_cost = cost + ((n+1) != grid[row][col])
            if new_cost < min_cost[r2][c2]:
                min_cost[r2][c2] = new_cost
                heapq.heappush(min_heap, (new_cost, r2, c2))
    return min_cost[num_row-1][num_col-1]


# print(minCost(grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]))
# print(minCost(grid = [[1,1,3],[3,2,2],[1,1,4]]))
print(minCost(grid = [[1,2],[4,3]]))

