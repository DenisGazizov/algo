def takeCharacters(s, k):
    d = {c: s.count(c) - k for c in 'abc'}
    if min(d.values()) < 0:
        return -1
    l, m, let = 0, 0, {'a': 0, 'b': 0, 'c': 0}
    for r, v in enumerate(s):
        let[v] += 1
        while let[v] > d[v]:
            d[s[l]] += 1
            l += 1
        m = max(m, r-l+1)
    return len(s) - m


print(takeCharacters(s = "aabaaaacaabc", k = 2))
print(takeCharacters(s = "a", k = 1))
