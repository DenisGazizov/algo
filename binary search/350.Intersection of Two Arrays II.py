def intersect(nums1, nums2):
    hash_list1 = {}
    res = []
    for i in nums1:
        hash_list1[i] = hash_list1.get(i, 0) + 1
    for j in nums2:
        if j in hash_list1 and hash_list1.get(j, 0) > 0:
            res.append(j)
            hash_list1[j] -= 1
    return res
print(intersect([4,9,5], [9,4,9,8,4]))