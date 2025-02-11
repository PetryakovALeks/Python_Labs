import re

def find_dates(text):
    # Регулярное выражение для поиска дат в формате "31 февраля 2007"
    pattern = r'\b(\d{1,2})\s+(января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)\s+(\d{4})\b'
    
    # Поиск всех совпадений в тексте
    matches = re.findall(pattern, text)
    
    # Возвращаем список найденных дат
    return [f"{match[0]} {match[1]} {match[2]}" for match in matches]

# Пример использования
text = "Вот несколько дат: 31 февраля 2007, 10.01.1994."
dates = find_dates(text)
print(dates)