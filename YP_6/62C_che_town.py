def func(n, r, array):
    left, right, ans = 0, 1, 0
    while right < n:
        if array[right] - array[left] > r:
            left += 1
            ans += n-right
        else:
            right += 1
    return ans


n, r = map(int, input().split())
array = list(map(int, input().split()))
print(func(n, r, array))