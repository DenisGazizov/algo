from typing import List


def findLengthOfShortestSubarray(arr: List[int]) -> int:
    ln = len(arr)
    if ln == 1:
        return 0
    l, r = 0, ln - 1
    pref, suff = 1, 1
    while l < ln - 1 or r > 0:
        if arr[l] < arr[l+1]:
            pref += 1
            l += 1
        else:
            l = ln
        if arr[r] > arr[r-1]:
            suff += 1
            r -= 1
        else:
            r = 0
    
    return pref, suff


print(findLengthOfShortestSubarray([1,2,3,10,4,2,3,5]))