import random as r
import time

variants = ['камень', 'ножницы', 'бумага']
win_comp = 0
win_player = 0
rounds = 2

print('Давай сыграем в "Камень-ножницы-бумага"!!!')
time.sleep(1)
print(f'Играем до {rounds} побед.')
time.sleep(1)

while win_comp < rounds and win_player < rounds:
    comp_choice = r.choice(variants)
    player_choice = (input("Ваш выбор: ")).lower().split()
    player_choice = "".join(player_choice)
    # Условия
    if (player_choice != comp_choice and
        player_choice == 'камень' and
        comp_choice == 'ножницы'):
            win_player += 1
    elif (player_choice != comp_choice and
            player_choice == 'камень' and
            comp_choice == 'бумага'):
                win_comp += 1
    elif (player_choice != comp_choice and
            player_choice == 'ножницы' and
            comp_choice == 'бумага'):
                win_player += 1
    elif (player_choice != comp_choice and
            player_choice == 'ножницы' and
            comp_choice == 'камень'):
                win_comp += 1
    elif (player_choice != comp_choice and
            player_choice == 'бумага' and
            comp_choice == 'камень'):
                win_player += 1
    elif (player_choice != comp_choice and
            player_choice == 'бумага' and
            comp_choice == 'ножницы'):
                win_comp += 1
    # Подведение итогов раунда
    time.sleep(1)
    print(f'Ваш счет: {win_player}')
    print(f'Счет противника: {win_comp}')
    if win_player > win_comp:
        print(f"Вы ПОБЕДИЛИ! Компьютер выбрал: {comp_choice}")
    elif win_player == win_comp:
        print(f'Ничья. Компьютер выбрал: {comp_choice}')
    else:
        print(f"Вы ПРОИГРАЛИ. Компьютер выбрал: {comp_choice}")
