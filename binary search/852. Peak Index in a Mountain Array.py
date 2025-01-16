from typing import List


def peakIndexInMountainArray(arr: List[int]) -> int:
    left, right = 0, len(arr)
    while left <= right:
        mid = (right + left) // 2
        temp_mid = arr[mid]
        if temp_mid > arr[mid-1] and temp_mid > arr[mid+1]:
            return mid
        elif temp_mid < arr[mid-1]:
            right = mid
        else:
            left = mid


print(peakIndexInMountainArray([11, 10, 7, 6, 5, 4, 3, 2]))
print(peakIndexInMountainArray([0,2,1,0]))
print(peakIndexInMountainArray([0,1,0]))
