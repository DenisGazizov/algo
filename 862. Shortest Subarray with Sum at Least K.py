from typing import List


def shortestSubarray(nums: List[int], k: int) -> int:
    ln = len(nums)
    prefix = [0] * (ln + 1)
    mx = float('inf')
    for i in range(ln):
        prefix[i+1] = nums[i] + prefix[i]
    for i in range(1, ln + 1):



shortestSubarray([2,-1,2], 4)

max