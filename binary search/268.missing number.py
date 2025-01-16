def missingNumber(nums):
    n = len(nums)
    summ = n * (n + 1) // 2
    for i in nums:
        summ -= i
    return summ

print(missingNumber([1, 2, 3, 0, 5, 6, 7]))
print(missingNumber([0, 1]))
print(5 ^ 5)

res = 0
for i in [1, 2, 3, 0, 5, 6, 7]:
    res ^= i
print(res)