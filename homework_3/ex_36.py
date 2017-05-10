import string

life = 9
word = input("Загадываемое слово: ")
word_g = word

while life > 0:
	alph = string.ascii_lowercase
	letter = input("Ваша буква: ")
	if (letter in alph and
		letter in word):
			index = (word.index(letter)) + 1
			print(f"Данная буква {index} в слове.")
			word = word.replace(letter, '0')
	else:
		life -= 1
		print("Буквы нет в слове")
		print(f"У вас осталось {life} жизней.")
		
	if life > 0 and word.count('0') == len(word_g):
		print("Вы победили!!!")
		print(f"Загаданное слово: {word_g}")
		exit()
		
print("Вы проиграли.")
exit()
