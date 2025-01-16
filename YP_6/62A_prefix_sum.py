def func(n, array):
    ans, summ = [], 0
    for i in range(n):
        ans.append(summ+array[i])
        summ += array[i]
    return ans

n = int(input())
array = list(map(int, input().split()))
print(*func(n, array))
