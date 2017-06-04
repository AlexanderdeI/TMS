import random
import time
import os

words = ["питон", "цикл", "исключение", "функция", "список"]

lives = 9
word = list(random.choice(words))
alph = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
game_word = list(("_" * len(word)))
tried_letters = []


def clear_display():
    time.sleep(1)
    os.system('cls')


def statistics_message():
    print("В слове {0} букв".format(len(word)))
    print("У вас {0} жизней.".format(lives))
    print(" ".join(game_word), end=2 * '\n')


while lives > 0:
    statistics_message()
    letter = (input("Ваша буква: ")).lower()

    if letter not in alph:
        print("Неправильный ввод")
        clear_display()
        continue

    elif letter in tried_letters:
        if letter.upper() not in word:
            print('Вы уже пробовали эту букву. Её нет в слове')
            clear_display()
            continue
        print('Вы уже отгадали эту букву')
        clear_display()
        continue

    elif letter in alph and letter in word:
        tried_letters.append(letter)
        for l in word:
            if l == letter:
                index = word.index(l)
                word[index] = l.upper()
                game_word.insert(index, l.upper())
                game_word.pop(index + 1)
        print('Есть такая буква!!!')
        clear_display()

    else:
        tried_letters.append(letter)
        lives -= 1
        print("Такой буквы нет", end='\r')
        clear_display()

    if lives > 0 and "".join(game_word).count('_') == 0:
        print("Вы победили!!!")
        print("Загаданное слово: " + " ".join(game_word))
        exit()

print('Вы проиграли :(')
