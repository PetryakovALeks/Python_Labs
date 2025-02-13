def find_two_min_indices(arr):
    if len(arr) < 2:
        raise ValueError("Массив должен содержать как минимум два элемента")

    min1 = 0  # Индекс первого наименьшего элемента
    min2 = 1  # Индекс второго наименьшего элемента

    # Если arr[min2] меньше arr[min1], меняем их местами
    if arr[min2] < arr[min1]:
        min1, min2 = min2, min1

    for i in range(2, len(arr)):
        if arr[i] < arr[min1]:
            min2 = min1
            min1 = i
        elif arr[i] < arr[min2]:
            min2 = i

    return min1, min2

# Пример использования
arr = [1, 13, 1, 10, 34, 1]
index1, index2 = find_two_min_indices(arr)
print(f"Индексы двух наименьших элементов: {index1}, {index2}")