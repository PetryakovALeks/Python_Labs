def sort(s):
    lovr_ = [char for char in s if char.islower()]  # Фильтруем строчные символы
    
    # Если нет строчных символов, возвращаем True (пустая последовательность считается упорядоченной)
    if not lovr_:
        return True
    
    # Проверяем, отсортированы ли символы по возрастанию
    for i in range(1, len(lovr_)):
        if lovr_[i] < lovr_[i - 1]:
            return False
    return True

# Примеры использования
print(sort("ABCDEfg"))  # True (строчные символы "f", "g" упорядочены)
  