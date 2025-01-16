def func(n, w, s):
    if len(s) == n:
        return s
    brack = {'(': ')', '[': ']'}
    s = list(s)
    stack = []
    for i in s:
        if stack and i == brack[stack[-1]]:
            stack.pop()
        else:
            stack.append(i)
    while n - len(s) > len(stack):
        for v in w:
            if stack and v == brack[stack[-1]]:
                s.append(brack[stack.pop()])
                break
            elif v in brack:
                s.append(v)
                stack.append(v)
                break
    while stack:
        s.append(brack[stack.pop()])

    return ''.join(s)

n = int(input())
w = input()
s = input()
print(func(n, w, s))
