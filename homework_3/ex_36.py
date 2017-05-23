import random as r

list_of_words = ['питон', 'цикл', 'функция', 'модуль',
				'словарь', 'исключение', 'список', 'строка']
word = r.choice(list_of_words)
len_word = len(word)
print(f'В слове {len_word} букв.')
word_g = (" _ " * len_word).split()
print(" ".join(word_g))
life = 9

while life > 0:
    alph = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    letter = input("Ваша буква: ")
    # Отгаданные буквы будем заменять на 0
    if (letter in alph and
        letter in word):
            index = (word.index(letter)) + 1
            print(f"Данная буква {index} в слове.")
            word_g[index - 1] = letter.upper()
            print(" ".join(word_g))
    else:
        life -= 1
        print("Буквы нет в слове")
        print(f"У вас осталось {life} жизней.")

    if life > 0 and ("".join(word_g)).count('_') == 0:
        print("Вы победили!!!")
        final_word = "".join(word_g)
        print(f'Загаданное слово: {final_word}')
        exit()

print("Вы проиграли.")

