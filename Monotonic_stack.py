massive = [73, 74, 75, 71, 69, 72, 76, 73]

def mon_stack(massive):
    ln = len(massive)
    stack = []
    ans = [0] * ln
    for i in range(ln):
        temp = massive[i]
        if stack and temp <= massive[stack[-1]]:
            stack.append(i)
        else:
            while stack and temp > massive[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
    return ans

print(mon_stack(massive))