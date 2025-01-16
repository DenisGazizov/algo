def func(n, m):
    if n == 1:
        return 0
    for i in range(1, n):
        if m[i] < m[i-1]:
            return -1
    return m[-1] - m[0]


n = int(input())
m = list(map(int, input().split()))
print(func(n, m))


