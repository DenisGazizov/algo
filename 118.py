from typing import List


def generate(numRows: int) -> List[List[int]]:
    res = []
    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = res[i - 1][j - 1] + res[i - 1][j]
        res.append(row)
    return res


print(generate(1))
print(generate(2))
print(generate(3))
print(generate(4))
print(generate(5))