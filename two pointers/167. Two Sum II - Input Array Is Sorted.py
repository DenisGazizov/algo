from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        summ = numbers[left] + numbers[right]
        if summ == target:
            return [left+1, right+1]
        elif summ > target:
            right -= 1
        else:
            left += 1



numbers1 = [2,7,11,15]
target1 = 9

numbers2 = [2,3,4]
target2 = 6

numbers3 = [-1,0]
target3 = -1
print(twoSum(numbers1, target1))
print(twoSum(numbers2, target2))
print(twoSum(numbers3, target3))
print(twoSum([-5,-3,0,2,4,6,8], 5))
print(twoSum([0,0,3,4], 0))
print(twoSum([-3,3,4,90], 0))
