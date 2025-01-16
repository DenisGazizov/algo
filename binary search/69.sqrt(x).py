def mySqrt(x: int) -> int:
    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        if x == mid * mid:
            return mid
        elif x > mid * mid:
            left = mid + 1
        elif x < mid * mid:
            right = mid - 1
    return right


print(mySqrt(0))
print(mySqrt(1))
print(mySqrt(2))
print(mySqrt(3))
print(mySqrt(9))
print(mySqrt(11))
print(mySqrt(2**31))
