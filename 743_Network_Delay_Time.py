import heapq
from typing import List


def networkDelayTime(times: List[List[int]], n: int, k: int) -> int:
    adj = {}
    for u, v, w in times:
        adj.setdefault(u, []).append((w, v))
    shortest = {}
    min_heap = [(0, k)]
    while min_heap:
        w1, u = heapq.heappop(min_heap)
        if u in shortest:
            continue
        shortest[u] = w1
        if u in adj:
            for w2, v in adj[u]:
                if v not in shortest:
                    heapq.heappush(min_heap, (w1 + w2, v))
        if len(shortest) == n:
            return max(shortest.values())
    return -1


print(networkDelayTime(times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2))
print(networkDelayTime(times = [[1,2,1]], n = 2, k = 1))
print(networkDelayTime(times = [[1,2,1]], n = 2, k = 2))

