def is_alternating(arr):
    if not arr:
        return False  # Пустой массив не подходит

    for i in range(len(arr) - 1):
        current_is_integer = isinstance(arr[i], int)
        next_is_float = isinstance(arr[i + 1], float)

        if not (current_is_integer and next_is_float):
            current_is_float = isinstance(arr[i], float)
            next_is_integer = isinstance(arr[i + 1], int)

            if not (current_is_float and next_is_integer):
                return False

    return True

# Пример использования:
arr1 = [1, 2.5, 3, 4.5, 5]
arr2 = [1, 2, 3.5, 4, 5.5]
arr3 = [1.5, 2, 3.5, 4, 5.5]

print(is_alternating(arr1))  # True
print(is_alternating(arr2))  # False
print(is_alternating(arr3))  # False