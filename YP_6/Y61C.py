def func():
    def presentation(some_matrix):
        str_bs = ''
        for i in some_matrix:
            temp_str = ''
            for j in i:
                if not temp_str:
                    temp_str += j
                if not temp_str[-1] == j:
                    temp_str += j
            if not str_bs:
                str_bs += temp_str
            else:
                str_bs += f',{temp_str}'
        return str_bs

    proection_str = {
        '#:#': "I",
        '#,#.#,#:#,#.#,#': "O",
        '#,#.,#:#,#.#': "C",
        '#.,#:#,.#': "L",
        '#.#,#,#.#:#,.#.,#': "H",
        '#,#.#,#,#.:#,#.#.,#.': "P"
    }
    n = int(input())
    matrix_bs = []
    for y in range(n):
        line = input()
        if not matrix_bs:
            matrix_bs.append(line)
        elif line != matrix_bs[-1]:
            matrix_bs.append(line)
    if len(matrix_bs) > 1 and set(matrix_bs[0]) == {'.'}:
        matrix_bs.pop(0)
    if len(matrix_bs) > 1 and set(matrix_bs[-1]) == {'.'}:
        matrix_bs.pop(-1)
    matrix_col = [i for i in zip(*matrix_bs)]
    rot_matrix = []
    for row in matrix_col:
        row = ''.join(row)
        if not rot_matrix:
            rot_matrix.append(row)
        elif row != rot_matrix[-1]:
            rot_matrix.append(row)
    if len(rot_matrix) > 1 and set(rot_matrix[0]) == {'.'}:
        rot_matrix.pop(0)
    if len(rot_matrix) > 1 and set(rot_matrix[-1]) == {'.'}:
        rot_matrix.pop(-1)
    res_matrix = [i for i in zip(*rot_matrix)]
    res = presentation(res_matrix) + ':' + presentation(rot_matrix)
    return proection_str.get(res, 'X')

print(func())

# with open('input2.txt', 'r', encoding='utf-8') as file:
#     tests = file.read().split('\n\n')
#     for i in tests:
#         test = i.split('\n')
#         n = func(test)
#         if test[-1] == n:
#             print('Test OK')
#         else:
#             print(f'Test {i} не сработал. Результат {n}, а должен быть {test[-1]}.')

