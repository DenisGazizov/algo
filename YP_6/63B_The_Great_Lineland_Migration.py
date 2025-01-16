def func(n, m):
    mon_stack = []
    result = [-1] * n
    for i in range(n):
        while mon_stack and mon_stack[-1][0] > m[i]:
            temp = mon_stack.pop()
            result[temp[1]] = i
        mon_stack.append([m[i], i])
    if mon_stack:
        for j in mon_stack:
            result[j[1]] = -1
    return result


n = int(input())
m = list(map(int, input().split()))
print(*func(n, m))
