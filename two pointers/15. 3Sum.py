from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    ans = []
    nums.sort()
    l1, l2, l3 = 0, 1, len(nums) - 1






print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))
print(threeSum([]))
print(threeSum([-10**5, -1, 0, 0, 1, 6, 10**5]))
print(threeSum([0,0,0,0]))
