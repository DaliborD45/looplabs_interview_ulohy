def remove_duplicates(arr):

    duplicates = []
    duplicates_index = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j] and j not in duplicates_index:
                duplicates.append(arr[j])
                duplicates_index.append(j)
    for duplicate_element in duplicates:
        arr.remove(duplicate_element)
    return arr


print(remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8,
      9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ]))
print(remove_duplicates([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


print(remove_duplicates([1, 1, 1, 1, 1, 1, 2]))