def romanToInt(s: str) -> int:
    hmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    length = len(s)-1
    res = 0
    for i in range(length+1):
        if i == 0:
            res += hmap[s[length]]
        elif hmap[s[length - i]] < hmap[s[length - i + 1]]:
            res -= hmap[s[length - i]]
        else:
            res += hmap[s[length - i]]
    return res

print(romanToInt(input()))
