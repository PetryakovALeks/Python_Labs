def calculate_mean_ascii_weight(s):
    """Вычисляет средний вес ASCII-кода символов строки."""
    # Суммируем ASCII-коды всех символов строки и делим на длину строки
    return sum(ord(char) for char in s) / len(s)

def max_triplet_mean(s):
    """Находит максимальное среднее значение ASCII-кода среди троек подряд идущих символов."""
    max_mean = -1  # Инициализируем переменную для хранения максимального среднего значения
    for i in range(len(s) - 2):  # Проходим по всем индексам строки, где можно взять тройку символов
        triplet = s[i:i+3]  # Выделяем тройку подряд идущих символов
        mean = calculate_mean_ascii_weight(triplet)  # Вычисляем средний вес ASCII-кода для этой тройки
        if mean > max_mean:  # Если текущее среднее больше максимального
            max_mean = mean  # Обновляем максимальное среднее значение
    return max_mean  # Возвращаем максимальное среднее значение среди всех троек

def calculate_quadratic_deviation(mean1, mean2):
    """Вычисляет квадратичное отклонение между двумя средними значениями."""
    # Возвращаем квадрат разности между двумя средними значениями
    return (mean1 - mean2) ** 2

def sort_strings_by_deviation(strings):
    """Сортирует строки по возрастанию квадратичного отклонения."""
    if not strings:  # Если список строк пуст
        return []  # Возвращаем пустой список

    # Создаем список кортежей (строка, квадратичное отклонение)
    strings_with_deviation = []
    for s in strings:  # Проходим по каждой строке в списке
        mean_string = calculate_mean_ascii_weight(s)  # Вычисляем средний вес ASCII-кода строки
        max_triplet = max_triplet_mean(s)  # Находим максимальное среднее значение ASCII-кода среди троек
        deviation = calculate_quadratic_deviation(mean_string, max_triplet)  # Вычисляем квадратичное отклонение
        strings_with_deviation.append((s, deviation))  # Добавляем кортеж (строка, отклонение) в список

    # Сортируем список кортежей по квадратичному отклонению (второй элемент кортежа)
    strings_with_deviation.sort(key=lambda x: x[1])

    # Возвращаем отсортированный список кортежей (строка, отклонение)
    return strings_with_deviation

# Пример использования
strings = ["abc", "defg", "hijkl", "mnopqr"]  # Входной список строк
sorted_strings_with_deviation = sort_strings_by_deviation(strings)  # Сортируем строки по отклонению

# Выводим отсортированный список строк с квадратичными отклонениями
for s, deviation in sorted_strings_with_deviation:
    print(f"Строка: {s}, Квадратичное отклонение: {deviation}")