def main():
    # Ввод максимального числа
    max_number = int(input())
    # Начальное множество возможных чисел
    possible_numbers = set(range(1, max_number + 1))

    while True:
        question = input().strip()
        if question == "HELP":
            break

        # Преобразуем вопрос в множество чисел
        numbers = set(map(int, question.split()))

        # Проверяем, является ли вопрос ровно половиной возможных чисел
        if len(numbers) == len(possible_numbers) / 2:
            # Август всегда отвечает NO в этом случае
            print("NO")
            # Убираем числа из возможных
            possible_numbers -= numbers
        else:
            # Считаем, сколько чисел останется при ответе YES и NO
            yes_option = possible_numbers & numbers
            no_option = possible_numbers - numbers

            # Август выбирает ответ, который оставляет больше чисел
            if len(yes_option) >= len(no_option):
                print("YES")
                possible_numbers = yes_option
            else:
                print("NO")
                possible_numbers = no_option

    # Выводим оставшиеся возможные числа
    print(" ".join(map(str, sorted(possible_numbers))))

if __name__ == "__main__":
    main()