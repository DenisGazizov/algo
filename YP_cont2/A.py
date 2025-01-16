def func(matrix, R, C):
    words = []
    for row in matrix:
        for word in row.split('#'):
            if len(word) >= 2:
                words.append(word)
    for c in range(C):
        current_word = []
        for r in range(R):
            char = matrix[r][c]
            if char != '#':
                current_word.append(char)
            else:
                if len(current_word) >= 2:
                    words.append(''.join(current_word))
                current_word = []
        if len(current_word) >= 2:
            words.append(''.join(current_word))
    return min(words)


R, C = map(int, input().split())
matrix = [input().strip() for _ in range(R)]
print(func(matrix, R, C))

