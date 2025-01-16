def func(n, array):
    array.sort()
    ans = n * [0]
    i = 0
    if n % 2 == 0:
        left, right = n // 2 - 1, n // 2
    else:
        left = right = n // 2
    while i < n:
        if left == right:
            ans[i] = array[left]
            left -= 1
            right += 1
            i += 1
        else:
            ans[i] = array[left]
            ans[i+1] = array[right]
            left -= 1
            right += 1
            i += 2
    return ans


n = int(input())
array = list(map(int, input().split()))
print(*func(n, array))