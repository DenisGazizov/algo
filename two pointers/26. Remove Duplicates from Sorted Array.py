from typing import List


def removeDuplicates(nums: List[int]) -> int:
    p1, p2 = 0, 1
    while p2 < len(nums):
        curr_digit = nums[p1]
        if nums[p2] != curr_digit:
            p1 += 1
            if p1 != p2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
            p2 += 1
        else:
            p2 += 1
    return p1 + 1


print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
print(removeDuplicates([1,1,2]))
