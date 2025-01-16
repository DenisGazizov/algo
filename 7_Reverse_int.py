from typing import List


def maximumBeauty(nums: List[int], k: int) -> int:
    const = k * 2
    nums.sort()
    l, r, res = 0, 0, 0
    while l<=r and r < len(nums):
        r += 1
        if r < len(nums) and nums[r] - nums[l] <= const:
            res = max(res, r-l)
        else:
            l += 1
    return res+1







print(maximumBeauty([4,6,1,2], 2))
print(maximumBeauty([1,1,1,1], 10))
print(maximumBeauty([27,55], 1))