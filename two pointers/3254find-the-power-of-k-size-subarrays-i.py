from typing import List


def resultsArray(nums: List[int], k: int) -> List[int]:
    res = [-1] * (len(nums) - k + 1)
    l, r = 0, 0
    yes = False
    while l < len(nums) - k:
        while r - l <= k-1 and r < len(nums) - 1:
            r += 1
            if nums[r] - nums[r-1] == 1:
                yes = True
            else:
                yes = False
        if yes:
            res[l] = nums[r]
        l += 1
    return res

print(resultsArray([1,2,3,4,3,2,5], k = 3))
