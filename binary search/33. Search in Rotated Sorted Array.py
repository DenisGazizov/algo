from typing import List


def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        temp = nums[mid]
        if temp == target:
            return mid
        if nums[left] <= temp:
            if nums[left] <= target <= temp:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if temp <= target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1





print(f'Answer: {search([4,5,6,7,0,1,2], 0)}, should be 4')
print(f'Answer: {search([4,5,6,7,0,1,2], 3)}, should be -1')
print(f'Answer: {search([3, 1], 1)}, should be 1')
print(f'Answer: {search([1], 1)}, should be 0')
print(f'Answer: {search([5, 6, 7, 8, 1, 2, 3], 1)}, should be 4')

