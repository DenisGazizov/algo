def func(N, B, A):
    pos_b = A.index(B)
    prefix_count_r = {}
    prefix_count_l = {}
    prefix = 0
    res = 1
    for i in range(pos_b-1, -1, -1):
        if A[i] < B:
            prefix -= 1
            if prefix in prefix_count_l:
                prefix_count_l[prefix] += 1
            else:
                prefix_count_l[prefix] = 1
        elif A[i] > B:
            prefix += 1
            if prefix in prefix_count_l:
                prefix_count_l[prefix] += 1
            else:
                prefix_count_l[prefix] = 1
    prefix = 0
    for j in range(pos_b+1, N):
        if A[j] < B:
            prefix += 1
            if prefix in prefix_count_r:
                prefix_count_r[prefix] += 1
            else:
                prefix_count_r[prefix] = 1
        elif A[j] > B:
            prefix -= 1
            if prefix in prefix_count_r:
                prefix_count_r[prefix] += 1
            else:
                prefix_count_r[prefix] = 1
    for k in prefix_count_r:
        if k in prefix_count_l:
            res += prefix_count_r[k] * prefix_count_l[k]
    if 0 in prefix_count_r:
        res += prefix_count_r[0]
    if 0 in prefix_count_l:
        res += prefix_count_l[0]
    return res


N, B = map(int, input().split())
A = list(map(int, input().split()))
print(func(N, B, A))