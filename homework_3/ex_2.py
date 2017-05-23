import random as r

start = 1
end = 100
rand_n = r.randint(start, end)

for n in range(end):
    # Число, которое предполагает пользователь
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
        
