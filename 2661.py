from typing import List


def firstCompleteIndex(arr: List[int], mat: List[List[int]]) -> int:
    n_rows, n_cols = len(mat), len(mat[0])
    hash_map = {}
    map_row, map_col = {}, {}
    for r in range(len(mat)):
        map_row[r] = 0
        for c in range(len(mat[0])):
            map_col[c] = 0
            hash_map[mat[r][c]] = (r, c)
    for i in range(len(arr)):
        r2, c2 = hash_map[arr[i]]
        map_row[r2] += 1
        map_col[c2] += 1
        if map_row[r2] == n_cols or map_col[c2] == n_rows:
            return i

print(firstCompleteIndex(arr = [1,3,4,2], mat = [[1,4],[2,3]]))
print(firstCompleteIndex(arr = [2,8,7,4,1,3,5,6,9], mat = [[3,2,5],[1,4,6],[8,7,9]]))
