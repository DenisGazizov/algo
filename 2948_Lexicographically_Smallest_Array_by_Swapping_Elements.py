from typing import List


def lexicographicallySmallestArray(nums: List[int], limit: int) -> List[
    int]:
    s_arr = sorted(nums)
    hash_map = {0: [[s_arr[0]], 0]}
    val_to_group = {s_arr[0]: 0}
    g = 0
    for i in range(1, len(s_arr)):
        if s_arr[i] - s_arr[i - 1] > limit:
            g += 1
        hash_map.setdefault(g, [[], 0])[0].append(s_arr[i])
        val_to_group[s_arr[i]] = g
    for j in range(len(nums)):
        group = val_to_group[nums[j]]
        pointer = hash_map[group][1]
        s_arr[j] = hash_map[group][0][pointer]
        hash_map[group][1] += 1
    return s_arr


# print(lexicographicallySmallestArray(nums = [1,5,3,9,8], limit = 2))
print(lexicographicallySmallestArray(nums = [4,3,23,84,34,88,44,44,18,15], limit = 3))