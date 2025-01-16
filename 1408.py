from typing import List


def stringMatching(words: List[str]) -> List[str]:
    n = sorted(words, key=len)
    ln = len(n) - 1
    res = []
    for i in range(ln):
        for s in range(i + 1, ln+1):
            if n[s].__contains__(n[i]):
                res.append(n[i])
                break
    return res

print(stringMatching(words = ["mass","as","hero","superhero"]))
