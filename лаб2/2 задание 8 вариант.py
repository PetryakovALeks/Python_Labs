def create_latin_english_dict(english_latin_dict):
    latin_english_dict = {}

    for english_word, latin_translations in english_latin_dict.items():
        for latin_word in latin_translations:
            if latin_word not in latin_english_dict:
                latin_english_dict[latin_word] = []
            latin_english_dict[latin_word].append(english_word)

   
    for latin_word in latin_english_dict:
        latin_english_dict[latin_word].sort()

   
    sorted_latin_english_dict = dict(sorted(latin_english_dict.items()))

    return sorted_latin_english_dict

def main():
    N = int(input())
    english_latin_dict = {}

    for _ in range(N):
        line = input().strip()
        english_word, translations = line.split(' - ')
        latin_translations = translations.split(', ')
        english_latin_dict[english_word] = latin_translations

    latin_english_dict = create_latin_english_dict(english_latin_dict)

    for latin_word, english_translations in latin_english_dict.items():
        print(f"{latin_word} - {', '.join(english_translations)}")

if __name__ == "__main__":
    main()
    
#3
#apple - malum, pomum, popula
#fruit - baca, bacca, popum
#punishment - malum, multa