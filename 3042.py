from typing import List


def countPrefixSuffixPairs(words: List[str]) -> int:
    def isPrefixAndSuffix(str1: str, str2: str) -> bool:
        if len(str1) >= len(str2):
            return False
        else:
            k, j = 0, len(str2) - len(str1)
            for i in range(len(str1)):
                if str1[i] != str2[k] or str1[i] != str2[j]:
                    return False
                k += 1
                j += 1
        return True

    c = 0
    for h in range(len(words) - 1):
        for g in range(h + 1, len(words)):
            if isPrefixAndSuffix(words[h], words[g]):
                c += 1
    return c


print(countPrefixSuffixPairs(["a","aba","ababa","aa"]))