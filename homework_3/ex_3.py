import random as r

start = 1
end = 10
rand_n = r.randint(start, end)
# Число попыток
tries = 3

for n in range(tries):
    user_n = int(input('Your number: '))
    while user_n != rand_n:
        if user_n > rand_n:
            print('The guesses number is little')
            break
        else:
            print('The guesses number is bigger')
            break
    else:
        print(f'You guess it!!! ({rand_n})')
        exit()
else:
    print('You lose(((\nTry again')
    exit()
