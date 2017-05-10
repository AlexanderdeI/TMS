import string
alph = string.ascii_lowercase

message = 'It is an encrypted message'
step = 10
new_message = ""
for el in message:
	if el == " ":
		el = el
		new_message += el
	elif ord(el) + step > ord('z'):
		new_message += chr(ord(el) + step - 26)
	else:
		new_message += chr(ord(el) + step)
		
print(new_message)
		
