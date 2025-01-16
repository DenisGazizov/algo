def func(arr):
    stack = []
    prefix_sum = [0]
    res = []
    for i in arr:
        sig = i[0]
        if sig == '-':
            res.append(stack.pop())
            prefix_sum.pop()
            continue
        value = int(i[1:])
        if sig == '+':
            stack.append(value)
            prefix_sum.append(prefix_sum[-1] + value)
        elif sig == '?':
            res.append(prefix_sum[-1] - prefix_sum[-(value+1)])
    return res


n = int(input())
arr = [input() for _ in range(n)]
print(*func(arr))
