def snail(snail_map):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    if not snail_map[0]:
        return []
    res = [snail_map[0][0]]
    snail_map[0][0] = '*'
    grid = len(snail_map) * len(snail_map[0])
    i = r = c = 0
    visited_r = set()
    visited_c = set()
    while i < grid:
        for a_r, a_c in directions:
            r += a_r
            c += a_c
            if a_c:
                visited_r.add(r)
            elif a_r:
                visited_c.add(c)
            while 0 <= r < len(snail_map) and 0 <= c < len(snail_map[0]) and snail_map[r][c] != '*':
                res.append(snail_map[r][c])
                snail_map[r][c] = '*'
                r += a_r
                c += a_c
            r -= a_r
            c -= a_c
            if a_r and r in visited_r:
                return res
            if a_c and c in visited_c:
                return res
    return res


def snail2(array):
    ret = []
    if array and array[0]:
        size = len(array)
        for n in range((size + 1) // 2):
            for x in range(n, size - n):
                ret.append(array[n][x])
            for y in range(1 + n, size - n):
                ret.append(array[y][-1 - n])
            for x in range(2 + n, size - n + 1):
                ret.append(array[-1 - n][-x])
            for y in range(2 + n, size - n):
                ret.append(array[-y][n])
    return ret



print(snail([[1,2,3],
             [4,5,6],
             [7,8,9]]))
print(snail([[1,2],
             [4,5]]))
print(snail([[1]]))
print(snail([[]]))
print(snail([[1,2,3]]))
print(snail([[1],[2],[3]]))