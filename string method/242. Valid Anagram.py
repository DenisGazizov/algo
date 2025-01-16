def isAnagram(s: str, t: str) -> bool:
    hashmap = {}
    for i in s:
        hashmap[i] = hashmap.setdefault(i, 0) + 1
    for j in t:
        hashmap[j] = hashmap.setdefault(j, 0) - 1
    return all(v == 0 for v in hashmap.values())


print(isAnagram('anagram', "nagaramd"))