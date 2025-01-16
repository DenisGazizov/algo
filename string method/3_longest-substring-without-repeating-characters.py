def lengthOfLongestSubstring(s: str) -> int:
    hash_map = {}
    left = 0
    mx = 0
    tmp_mx = 0
    for i, v in enumerate(s):
        if v not in hash_map:
            hash_map.setdefault(v, []).append(i)
            tmp_mx += 1
        else:
            left = hash_map[v][-1]
            hash_map[v].append(i)
            tmp_mx = i - left
        if tmp_mx > mx:
            mx = tmp_mx
    return mx


# print(lengthOfLongestSubstring('pwwkew'))
# print(lengthOfLongestSubstring('bbbbb'))
# print(lengthOfLongestSubstring('abcabcbb'))
print(lengthOfLongestSubstring('abba'))
