from random import choice
from decouple import config


def game():
    numbers = list(range(1, 31))
    win_number = choice(numbers)
    win_sum = 0
    win_counter = 0
    money = float(config("MY_MONEY"))
    pick = input("Хотите сыграть еще раз? (да/нет): ")

    def play_again():
        if pick == 'да':
            print('игра оконченна')
            return True
        else:
            return False

    while pick:

        print(f'Ваш текущий баланс {money}')

        bet = int(input('Введите число: '))


        if bet > money:
            print("У вас недостаточно денег.")
            break


        choce_number = int(input('Выберите число от 1 до 30:'))

        if choce_number not in numbers:
            print('такого числа нет выберите число от 1 до 30:')


        if choce_number == win_number:
            money += bet * 2
            win_sum += bet * 2
            win_counter += 1
            print(f"Победа! Вы выйграли {bet * 2} "
                  f"Dаш общий выйгрыш составил {win_sum}:")

        else:
            money -= bet
            print(f"Вы проиграли, вы проиграли вашу ставку в размере {bet}")
        print(f'Победное число: {win_number}')




        if not play_again:
            break

print(game())


