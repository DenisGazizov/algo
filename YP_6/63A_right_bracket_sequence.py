def func(s):
    brackets = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for i in s:
        if i in brackets:
            stack.append(i)
        else:
            if stack and brackets[stack[-1]] == i:
                stack.pop()
            else:
                return 'no'
    if stack:
        return 'no'
    return 'yes'



print(func('()[]'))
print(func('([)]'))
print(func('('))
print(func('({[]})'))
print(func('({[]})'))
print(func('({([)]})'))
print(func(')}]({['))


