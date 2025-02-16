def is_prime(n):
    """Проверка, является ли число простым."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def average_of_non_primes_above_primes_average(lst):
    # Находим простые числа и их среднее арифметическое
    primes = [x for x in lst if is_prime(x)]
    if not primes:
        return 0  # Если простых чисел нет, возвращаем 0
    primes_avg = sum(primes) / len(primes)

    # Находим непростые числа, которые больше среднего простых
    non_primes = [x for x in lst if not is_prime(x) and x > primes_avg]

    # Вычисляем среднее арифметическое непростых чисел
    if not non_primes:
        return 0  # Если таких чисел нет, возвращаем 0
    return sum(non_primes) / len(non_primes)

# Пример использования
lst = [2, 3, 4, 5, 6, 7, 8, 9, 10]
result = average_of_non_primes_above_primes_average(lst)
print(result)  # Вывод: 7.0
print(result)  