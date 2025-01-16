def searchRange(nums, target):
    ans = [-1, -1]
    if len(nums) == 0:
        return ans
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        temp = nums[mid]
        if temp == target:
            ans[0] = ans[1] = mid
            break
        elif target > temp:
            left = mid + 1
        else:
            right = mid - 1
    if ans != [-1, -1]:
        i, j = ans[0] - 1, ans[0] + 1
        while i >= 0:
            if nums[i] == target:
                ans[0] = i
                i -= 1
            else:
                i = -1
        while j < len(nums):
            if nums[j] == target:
                ans[1] = j
                j += 1
            else:
                j = len(nums) + 1
    return ans


# print(searchRange(nums = [5,7,7,8,8,10], target = 8), f'Right ans: [3,4]')
# print(searchRange(nums = [5,7,7,8,8,10], target = 6), f'Right ans: [-1,-1]')
# print(searchRange(nums = [], target = 0), 'Right ans: [-1,-1]')
#print(searchRange(nums = [1], target = 0), 'Right ans: [-1,-1]')
print(searchRange(nums = [1], target = 1), 'Right ans: [0,0]')

