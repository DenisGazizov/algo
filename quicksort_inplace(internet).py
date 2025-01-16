from random import randint


def partition(array: list, left: int, right: int) -> int:
    rand = randint(left, right)
    array[rand], array[left] = array[left], array[rand]
    x = array[left]
    j = left
    for i in range(left + 1, right + 1):
        if array[i] <= x:
            j += 1
            array[j], array[i] = array[i], array[j]
    array[left], array[j] = array[j], array[left]
    return j


def quick_sort(array: list, left=0, right=None) -> None:
    if right is None:
        right = len(array) - 1
    if left < right:
        m = partition(array, left, right)
        quick_sort(array, left, m - 1)
        quick_sort(array, m + 1, right)

test_list = [10, 11, 15, 16,5,1,2,3,4,5,6,7,8,9,10]
quick_sort(test_list)
print(test_list)

