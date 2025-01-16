def partition(array, left, right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1


def quickSort(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left < right:
        pi = partition(array, left, right)
        quickSort(array, left, pi - 1)
        quickSort(array, pi + 1, right)

data = [1, 7, 4, 1, 10, 9, -2]
quickSort(data)
print(data)

