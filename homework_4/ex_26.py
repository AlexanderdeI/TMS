def input_text(n=2):
    # Если пользователь ввел два раза пустую строку => выход
    while n > 0:
        text = input()
        if text == '':
            n -= 1

input_text()
