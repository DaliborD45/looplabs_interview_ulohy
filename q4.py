def resolve_cycle(index, starting_point, arr):

    checked_indexes = [index]
    checked_ciselka = [starting_point]
    is_found = False
    while not is_found and len(checked_indexes) <= len(arr):
        move_index = checked_ciselka[-1]
        ciselko = arr[move_index]
        checked_ciselka.append(ciselko)

        checked_indexes.append(move_index)
        if ciselko == -1:
            break
        if move_index == index:
            is_found = True
    return is_found


def is_cycled(arr):
    is_found = False
    for i in range(len(arr)):
        result = resolve_cycle(i, arr[i], arr)
        if result:
            is_found = True
            break
        else:
            continue

    return is_found


print(is_cycled([1, 2, 3, 4, 5, 0]))
print(is_cycled([5, 4, 3, -1, 2, -1]))  # !
print(is_cycled([1, 2, 2, 4, 3, 1]))
print(is_cycled([0, -1, -1, -1, -1, -1]))
print(is_cycled([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, -1, 10]))  # !
print(is_cycled([1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 5, 10]))
