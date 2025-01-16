from typing import List


def sortColors(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    hash_map = [0] * 3
    for i in nums:
        hash_map[i] += 1
    idx = 0
    for item in range(3):
        count = hash_map[item]
        nums[idx : idx + count] = [item] * count
        idx += count

nums = [2,0,2,1,1,0]
sortColors(nums)
print(nums)