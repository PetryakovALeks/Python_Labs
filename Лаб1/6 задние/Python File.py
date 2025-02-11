import re

def find_lowercase_latin_chars(text):
    # Регулярное выражение для поиска строчных символов латиницы
    pattern = r'[a-z]'
    
    # Находим все совпадения
    matches = re.findall(pattern, text)
    
    # Возвращаем уникальные символы
    return sorted(set(matches))

# Пример использования
text = "Hello World! This is a test string with lowercase letters: a, b, c."
lowercase_chars = find_lowercase_latin_chars(text)
print(lowercase_chars)