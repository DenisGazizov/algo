from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    n = len(nums)
    result = []
    for i in range(1 << n):
        subset = []
        for j in range(n):
            s = i & (1 << j)
            if s:
                subset.append(nums[j])
        result.append(subset)
    return result

print(subsets([1, 2, 3]))