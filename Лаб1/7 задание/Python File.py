import re

def count_unique_latin_chars(text):
    # Находим все символы латиницы (строчные и заглавные)
    matches = re.findall(r'[a-zA-Z]', text)
    
    # Используем множество для хранения уникальных символов
    unique_chars = set(matches)
    
    # Возвращаем количество уникальных символов
    return len(unique_chars)

# Пример использования
text = "Hello World!  a, b, C, D."
unique_count = count_unique_latin_chars(text)
print(f"Количество уникальных символов латиницы: {unique_count}")