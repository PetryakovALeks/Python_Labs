def find_missing_numbers(arr, n):
    # Преобразуем массив в множество для быстрого поиска
    num_set = set(arr)
    missing_numbers = []

    # Проверяем все числа от 1 до n
    for i in range(1, n + 1):
        if i not in num_set:
            missing_numbers.append(i)

    return missing_numbers

# Пример использования
arr = [1, 2, 4, 6, 7, 9]
n = 100 # Максимальное число в диапазоне
missing = find_missing_numbers(arr, n)
print("Пропущенные числа:", missing)