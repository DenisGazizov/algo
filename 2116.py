def canBeValid(s: str, locked: str) -> bool:
    if len(s) % 2 == 1:
        return False
    stack, wildstack = [], []
    for i, p in enumerate(s):
        if locked[i] == '0':
            wildstack.append(i)
        elif p == '(':
            stack.append(i)
        elif p == ')':
            if stack:
                stack.pop()
            elif wildstack:
                wildstack.pop()
            else:
                return False
    while stack and wildstack and stack[-1] < wildstack[-1]:
        stack.pop()
        wildstack.pop()
    return not stack


# print(canBeValid("))()))", "010100"))
# print(canBeValid("()()", "0000"))
# print(canBeValid(")", "0"))
# print(canBeValid("((((((", "000000"))
# print(canBeValid("((((((", "111111"))
# print(canBeValid("((((((", "000111"))
# print(canBeValid("((((((", "111000"))
print(canBeValid("((()(()()))()((()()))))()((()(()",
                 "10111100100101001110100010001001"))