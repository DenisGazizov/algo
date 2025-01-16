from math import gcd, lcm


def func(a, b):
    n = gcd(a, b)
    if a > b:
        minim, maxim = b, a
    else:
        minim, maxim = a, b
    res = maxim // n
    return gcd(res, minim), lcm(res, minim)

t = int(input())
ans = []
for _ in range(t):
    a, b = map(int, input().split())
    ans.append(func(a, b))
print(*ans, sep='\n')