from collections import deque


def func(n, k, m):
    res = []
    deq = deque()
    st_pos = 0
    for i in range(n):
        x = m[i]
        while deq and x < deq[-1][0]:
            deq.pop()
        deq.append((x, i))
        while deq[st_pos][1] <= i-k:
            deq.popleft()
        if i >= (k-1):
            res.append(deq[0][0])
    return res


n, k = map(int, input().split())
m = list(map(int, input().split()))
print(*func(n, k, m), sep='\n')


# def func(n, k, m):
#     window = []
#     st_ind = 0
#     for i, x in enumerate(m):
#         while window and window[-1][0] > x:
#             window.pop()
#         window.append((x, i))
#         while window[0][1] <= i - k:
#             st_ind += 1
#         yield window[st_ind][0]
#
# n, k = map(int, input().split())
# m = list(map(int, input().split()))
# print(*func(n, k, m), sep='\n')
