def func(n, k, array):
    current = 0
    ans = 0
    sum_frequency = {0: 1}
    for i in range(n):
        current += array[i]
        target_sum = current - k
        if target_sum in sum_frequency:
            ans += sum_frequency[target_sum]
        sum_frequency[current] = sum_frequency.get(current, 0) + 1
    return ans


n, k = map(int, input().split())
array = list(map(int, input().split()))
print(func(n, k, array))

