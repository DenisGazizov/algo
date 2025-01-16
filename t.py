def count_subarrays_with_median_b(N, B, A):
    ind_b = A.index(B)
    result = 0
    for left in range(ind_b, -1, -1):
        for right in range(ind_b, N):
            if A[left] < B and A[right] > B:
                result += 1
    return result



N, B = map(int, input().split())
A = list(map(int, input().split()))
print(count_subarrays_with_median_b(N, B, A))