from typing import List


def subsets(nums: List[int]) -> List[List[int]]:
    res = []
    ln = len(nums)
    for i in range(1 << ln):
        temp = []
        for j in range(ln):
            if i & (1 << j):
                temp.append(nums[j])
        res.append(temp)
    return res


print(subsets([1,2,3]))



