from typing import List


def trap(height: List[int]) -> int:
    maximum = [0, 0]
    for i in range(len(height)):
        temp = height[i]
        if temp > maximum[1]:
            maximum[0] = i
            maximum[1] = temp
    res = 0
    monstack = []
    for i in range(maximum[0]):
        temp1 = height[i]
        if not monstack:
            monstack.append(temp1)
        elif temp1 > monstack[-1]:
            monstack.pop()
            monstack.append(temp1)
        elif temp1 < monstack[-1]:
            res += monstack[-1] - temp1
    monstack = []
    for j in range(len(height) - 1, maximum[0], -1):
        temp2 = height[j]
        if not monstack:
            monstack.append(temp2)
        elif temp2 > monstack[-1]:
            monstack.pop()
            monstack.append(temp2)
        elif temp2 < monstack[-1]:
            res += monstack[-1] - temp2
    return res


print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))