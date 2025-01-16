def func(n, c, array):
    prefix_b_pos = [0] * (n+1)
    count_b = 0
    for i in range(1, n+1):
        if array[i-1] == 'b':
            count_b += 1
        prefix_b_pos[i] = count_b
    left = result = pairs = 0
    for right in range(n):
        b_last = prefix_b_pos[n]
        if array[right] == 'a':
            pairs += b_last - prefix_b_pos[right]
        while pairs > c and left <= right:
            if array[left] == 'a':
                pairs -= b_last - prefix_b_pos[left]
            left += 1
        result = max(result, right - left + 1)

    return result



n, c = map(int, input().split())
array = input()
print(func(n, c, array))