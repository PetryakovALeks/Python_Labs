# Чтение списка строк с клавиатуры
strings = []
print("Введите строки (для завершения введите пустую строку):")
while True:
    line = input()
    if line == "":  # Если введена пустая строка, завершаем ввод
        break
    strings.append(line)

# Упорядочивание строк по количеству слов
sorted_strings = sorted(strings, key=lambda x: len(x.split()))

# Вывод результата
print("Упорядоченные строки по количеству слов:")
for s in sorted_strings:
    print(s)