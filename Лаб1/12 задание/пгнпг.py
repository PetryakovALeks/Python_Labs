def calculate_mean_ascii_weight(s):
    return sum(ord(char) for char in s) / len(s)

def calculate_quadratic_deviation(mean1, mean2):
    return (mean1 - mean2) ** 2

def sort_strings_by_deviation(strings):
    if not strings:
        return []

    # Вычисляем средний вес ASCII-кода первой строки
    first_mean = calculate_mean_ascii_weight(strings[0])

    # Создаем список кортежей (строка, квадратичное отклонение)
    strings_with_deviation = []
    for s in strings:
        mean = calculate_mean_ascii_weight(s)
        deviation = calculate_quadratic_deviation(first_mean, mean)
        strings_with_deviation.append((s, deviation))

    # Сортируем по квадратичному отклонению
    strings_with_deviation.sort(key=lambda x: x[1])

    # Возвращаем отсортированный список строк
    return [s for s, _ in strings_with_deviation]

# Пример использования
strings = ["abc", "def", "ghi", "jkl"]
sorted_strings = sort_strings_by_deviation(strings)
print(sorted_strings)