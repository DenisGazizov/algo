def partition(array, pivot):
    left, right, mid = [], [], []
    for i in array:
        if i == pivot:
            mid.append(i)
        elif pivot > i:
            left.append(i)
        elif pivot < i:
            right.append(i)
    return left, right, mid

def quicksort(array):
    print(f"Start quicksort with array:{array}")
    if len(array) < 2:
        print(f'Зашёл в if Длина массива {array} меньше 2')
        return array
    else:
        print(f"Зашёл в else.")
        pivot = array[len(array) // 2]
        print(f'Вызываю функцию partition с параметрами array = {array}, pivot = {pivot}')
        left, right, mid = partition(array, pivot)
        print(f'Результат L{left} + M{mid} + R{right}')
        return quicksort(left) + mid + quicksort(right)


print(quicksort([10, 11, 15, 16, 5, 6]))
