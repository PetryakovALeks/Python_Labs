def count_mirror_triplets(s):
    count = 0
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            count += 1
    return count #длинна строки

def average_mirror_triplets(s):
    if len(s) < 3:
        return 0
    return count_mirror_triplets(s) / (len(s) - 2)

def sort_strings_by_mirror_triplets(strings):
    return sorted(strings, key=average_mirror_triplets)


# Пример использования
strings = ["abc", "ada", "xyz", "abba", "level", "noon"]
sorted_strings = sort_strings_by_mirror_triplets(strings)
print(sorted_strings)