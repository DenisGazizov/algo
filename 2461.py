from typing import List


def maximumSubarraySum(nums: List[int], k: int) -> int:
    last_sum = 0
    hashmap = set()
    res, l = 0, 0
    for i in range(len(nums)):
        temp = nums[i]
        if temp not in hashmap:
            hashmap.add(temp)
        else:
            l += 1
        if i + 1 - l == k:
            if len(hashmap) == k:
                res = max(res, prefix_sum[i+1] - prefix_sum[l])
            hashmap[nums[l]] -= 1
            if hashmap[nums[l]] == 0:
                hashmap.pop(nums[l])
            l += 1
    return res


print(maximumSubarraySum([1,5,4,2,9,9,9], k = 3))
print(maximumSubarraySum([4,4,4], k = 3))