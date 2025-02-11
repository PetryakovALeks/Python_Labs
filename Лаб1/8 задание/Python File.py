import os

def get_filename_without_extension(filepath):
    return os.path.splitext(os.path.basename(filepath))[0]

# Пример
print(get_filename_without_extension("/home/user/docs/report.txt"))  # Вывод: report