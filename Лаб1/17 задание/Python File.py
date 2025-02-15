def count_local_maxima(arr):
    count = 0
    for i in range(1, len(arr) - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            count += 1
    return count

# Пример использования
array = [1, 3, 2, 4, 1, 5, 3, 2]
result = count_local_maxima(array)
print(f"Количество локальных максимумов: {result}")