def partition(array, left, right):
    pivot = array[(left+right) // 2]
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while array[i] < pivot:
            i += 1
        j -= 1
        while array[j] > pivot:
            j -= 1
        if i >= j:
            return j
        array[i], array[j] = array[j], array[i]


def quicksort_inplace(array, left=0, right=None):
    if right is None:
        right = len(array) - 1
    if left < right:
        pivot = partition(array, left, right)
        quicksort_inplace(array, left, pivot)
        quicksort_inplace(array, pivot + 1, right)

test_list = [10, 11, 15, 16, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quicksort_inplace(test_list)
print(test_list)
