from typing import List


def moveZeroes(nums: List[int]) -> None:
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]

            left += 1



moveZeroes([4, 5, 10, 19, 20, 0, 1, 0, 3, 12, 0])