def strStr(haystack: str, needle: str) -> int:
    lps = [0] * len(needle)
    pre = 0
    for i in range(1, len(needle)):
        while pre > 0 and needle[pre] != needle[i]:
            pre = lps[pre-1]
        if needle[pre] == needle[i]:
            pre += 1
            lps[i] = pre
    n = 0
    for j in range(len(haystack)):
        while n > 0 and needle[n] != haystack[j]:
            n = lps[n-1]
        if needle[n] == haystack[j]:
            n += 1
        if n == len(needle):
            return j - n + 1



def strStr1(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    else:
        return -1


# print(strStr(haystack = "leetcode", needle = "leeto"))
# print(strStr(haystack = "sadbutsad", needle = "sad"))
# print(strStr(haystack = "asadbutsad", needle = "sad"))
# print(strStr(haystack = "sakadbutsadd", needle = "sad"))
# print(strStr(haystack = "sakadbutsad", needle = "sad"))
# print(strStr(haystack = "aaa", needle = "aaaa"))
# print(strStr(haystack = "aaa", needle = "aaa"))
#print(strStr(haystack = "mississippi", needle = "issip"))
#print(strStr(haystack = "mississippi", needle = "issipi"))
#print(strStr(haystack = "mississippi", needle = "pi"))
#print(strStr(haystack = "bbaa", needle = "aab"))
#print(strStr(haystack = "aabaaabaaac", needle = "aabaaac"))
print(strStr(haystack = "abacabababad", needle = "ababad"))