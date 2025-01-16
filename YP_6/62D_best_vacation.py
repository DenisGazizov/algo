def func(n, k, array):
    array.sort()
    max_window = 0
    left, right = 0, 1
    while left < n:
        while right < n:
            if array[right] - array[left] <= k:
                right += 1
            else:
                break
        if (right - left) > max_window:
            max_window = (right - left)
        left += 1

    return max_window

n, k = map(int, input().split())
array = list(map(int, input().split()))
print(func(n, k, array))