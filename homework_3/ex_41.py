import string

low_lett = string.ascii_lowercase
upp_lett = string.ascii_uppercase
puct = string.punctuation

password = input("Password: ")
errors = []

for i in password:
	if (len(password) > 16 or
		len(password) < 6):
			e = "пароль не подходит по размеру"
			errors.append(e)
	if i not in low_lett: 
		e = 'нет маленьких букв'
		errors.append(e)
	if i not in upp_lett:
		e = 'нет больших букв'
		errors.append(e)
	if i not in puct:
		e = 'нет знаков пунктуации'
		errors.append(e)
		
print(set(errors))
