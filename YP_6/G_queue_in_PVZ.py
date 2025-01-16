def func(n, b, a):
    res = 0
    rem = 0
    for i in range(n):
        temp = a[i] + rem
        if temp <= b:
            res += temp
            rem = 0
        else:
            res += temp
            rem = temp - b
    res += rem
    return res


n, b = map(int, input().split())
a = list(map(int, input().split()))
print(func(n, b, a))
