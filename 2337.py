def canChange(start: str, target: str) -> bool:
    i, j = 0, 0
    ln = len(start)-1
    while i < ln or j < ln:
        while i < ln and start[i] == '_':
            i += 1
        while j < ln and target[j] == '_':
            j += 1
        c = start[i]
        if c != target[j]:
            return False
        if c == 'L' and i < j:
            return False
        if c == 'R' and i > j:
            return False
        i += 1
        j += 1
    return True


print(canChange("_L__R__R_", "L______RR"))
print(canChange("R_L_", "__LR"))
print(canChange("_R", "R_"))