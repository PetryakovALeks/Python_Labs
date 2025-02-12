# Чтение списка строк с клавиатуры
strings = []
print("Введите строки (для завершения введите пустую строку):")
while True:
    line = input()
    if line == "":  # Если введена пустая строка, завершаем ввод
        break
    strings.append(line)

# Функция для вычисления среднего веса ASCII-кода символов строки
def average_ascii_weight(s):
    """
    Вычисляет средний вес ASCII-кода символов строки.
    ASCII-код — это числовое представление символа в кодировке ASCII.
    Например, ASCII-код символа 'A' равен 65, 'a' — 97, '1' — 49.
    """
    if len(s) == 0:
        return 0  # Чтобы избежать деления на ноль для пустых строк
    # Функция ord(char) возвращает ASCII-код символа char
    return sum(ord(char) for char in s) / len(s)

# Упорядочивание строк по среднему весу ASCII-кода символов
sorted_strings = sorted(strings, key=average_ascii_weight)

# Вывод результата
print("Упорядоченные строки по среднему весу ASCII-кода символов:")
for s in sorted_strings:
    print(s)