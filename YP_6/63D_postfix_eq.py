def func(n):
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: y - x,
                 '*': lambda x, y: x * y}
    stack = []
    for i in n:
        if i in operators:
            stack.append(operators[i](stack.pop(), stack.pop()))
        else:
            stack.append(int(i))
    return stack

n = input().strip().split()
print(*func(n))
