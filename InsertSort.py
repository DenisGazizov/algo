def insertion_sort(array):
    for i in range(len(array)):
        item_to_insert = array[i]
        j = i
        while j > 0 and item_to_insert < array[j-1]:
            array[j] = array[j-1]
            j -= 1
        print(f'step {i}, sorted {i + 1} elements: {array}')
        array[j] = item_to_insert

    return array

print(insertion_sort([10, 11, 15, 16,5,1,2,3,4,5,6,7,8,9,10]))