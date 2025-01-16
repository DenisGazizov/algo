n, m = map(int, input().split())
a = sum(map(int, input().split()))
b = sum(map(int, input().split()))
if a <= m <= b:
    print('YES')
else:
    print('NO')


