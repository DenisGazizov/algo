def func(n, array):
    summ = 0
    prefix_sum = [0] * (n+1)
    prefix_ij = [0] * (n-1)
    for i in range(1, n+1):
        prefix_sum[i] += prefix_sum[i-1] + array[i-1]
    for j in range(1, n-1):
        prefix_ij[j] = prefix_ij[j-1] + array[j] * (prefix_sum[-1] - prefix_sum[j+1])
    for k in range(n-2):
        summ += array[k] * (prefix_ij[-1] - prefix_ij[k])

    return summ % 1000000007


n = int(input())
array = list(map(int, input().split()))
print(func(n, array))