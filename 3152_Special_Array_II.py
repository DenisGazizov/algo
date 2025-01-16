from typing import List


def isArraySpecial(nums: List[int], queries: List[List[int]]) -> List[
    bool]:
    sub_arr = []
    start, end = 0, 0
    res = []
    for i in range(1, len(nums)):
        if (nums[i] - nums[i - 1]) % 2 != 0:
            end += 1
        else:
            sub_arr.append([start, end])
            start = i
            end = i
    sub_arr.append([start, end])
    for q in queries:
        l, r = 0, len(sub_arr) - 1
        while l <= r:
            mid = (r + l) // 2
            val = sub_arr[mid]
            if q[0] < val[0]:
                r = mid - 1
            else:
                if q[0] > val[1]:
                    l = mid + 1
                elif q[1] <= val[1]:
                    res.append(True)
                    break
                else:
                    res.append(False)
                    break
    return res


print(isArraySpecial(nums = [4, 3, 1, 6], queries = [[0,2], [2,3]]))
print(isArraySpecial(nums = [3,4,1,2,6], queries = [[0,4]]))
