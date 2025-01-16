from typing import List


def shiftingLetters(s: str, shifts: List[List[int]]) -> str:
    prefix = [0] * len(s)
    for i in shifts:
        for j in range(i[0], i[1] + 1):
            if i[2] == 0:
                prefix[j] -= 1
            else:
                prefix[j] += 1
    for k in range(len(s)):
        if prefix[k] != 0:
            temp = ord('a') + (25 - (ord('z') - (ord(s[k]) + prefix[k])) % 26 )
            prefix[k] = chr(temp)
        else:
            prefix[k] = s[k]
    return ''.join(prefix)




s = 'hero'
c = 'superhero'
print(s in c)