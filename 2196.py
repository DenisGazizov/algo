def maximumLength(s: str) -> int:
    sub_arr = {}
    ln = len(s)
    res = -1
    for i in range(ln):
        ind, f_l = i+1, s[i]
        sub_arr[s[i]] = sub_arr.setdefault(s[i], 0) + 1
        while ind < len(s) and s[ind] == s[i]:
            f_l += s[ind]
            sub_arr[f_l] = sub_arr.setdefault(f_l, 0) + 1
            ind += 1
    for j in sub_arr:
        if sub_arr[j] >= 3:
            res = max(res, len(j))
    return res


print(maximumLength("aaaa"))
print(maximumLength("abcdef"))
print(maximumLength("abcaba"))