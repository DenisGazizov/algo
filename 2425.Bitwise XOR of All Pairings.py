from typing import List


def xorAllNums(nums1: List[int], nums2: List[int]) -> int:
    n, m, res = len(nums1), len(nums2), 0
    if n % 2 == 1:
        for i in nums2:
            res ^= i
    if m % 2 == 1:
        for j in nums1:
            res ^= j
    return res