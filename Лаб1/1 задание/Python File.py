import math

def cnt_prost(n):
    """Считает количество чисел от 1 до n, взаимно простых с n."""
    cnt = 0
    for i in range(1, n + 1):
        if math.gcd(i, n) == 1:
            cnt += 1
    return cnt  # Исправил отступ, return должен быть вне цикла.

def sum_na(number):
    """Вычисляет сумму цифр числа, делящихся на 3."""
    summa = 0
    number_str = str(abs(number))
    for di in number_str:
        di_int = int(di)
        if di_int % 3 == 0:
            summa += di_int
    return summa

# Пример использования:
number = 1234567890
sum_digits_divisible_by_3 = sum_na(number)
print(f"Сумма цифр числа {number}, делящихся на 3: {sum_digits_divisible_by_3}")
count_coprime = cnt_prost(sum_digits_divisible_by_3)
print(f"Количество чисел, взаимно простых с суммой цифр, делящихся на 3: {count_coprime}")
