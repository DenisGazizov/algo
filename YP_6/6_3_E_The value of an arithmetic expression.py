def func(n):
    operators = {'+': lambda x, y: x + y,
                 '-': lambda x, y: y - x,
                 '*': lambda x, y: x * y}
    postfix = []
    stack = []
    i = 0
    if n[-1] in '-+*(':
        return 'WRONG'
    for j in range(len(n)-1):
        if n[j] not in '0123456789-+*() ':
            return 'WRONG'
        if n[j] in '-+*(' and n[j+1] in '-+*)':
            return 'WRONG'
    while i <= len(n) - 1:
        if n[i] in operators:
            if n[i] in '+-':
                while stack and stack[-1] in '-+*':
                    postfix.append(stack.pop())
            elif n[i] == '*':
                while stack and stack[-1] == '*':
                    postfix.append(stack.pop())
            stack.append(n[i])
        elif n[i] in (')('):
            if n[i] == '(':
                stack.append(n[i])
            elif n[i] == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    return 'WRONG'
        elif n[i].isdigit():
            temp = ''
            while i <= (len(n) - 1) and n[i].isdigit():
                temp += n[i]
                i += 1
            postfix.append(int(temp))
            i -= 1
        i += 1
    while stack:
        if stack[-1] not in '()':
            postfix.append(stack.pop(-1))
        else:
            return 'WRONG'
    for k in postfix:
        if k in operators:
            stack.append(operators[k](stack.pop(), stack.pop()))
        else:
            stack.append(int(k))
    if len(stack) > 1:
        if stack[0] == '-':
            return ''.join(stack)
        else:
            return 'WRONG'
    return stack[0]

n = input()
print(func(n))
