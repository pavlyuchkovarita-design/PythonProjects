import random

comp_number = random.randint(1, 100)

is_run = True

while is_run == True:
    user_number = int(input("Введите своё число от 1 до 100: "))

    if user_number > comp_number:
        print("Введи поменьше")

    if user_number < comp_number:
            print("Введи побольше")

    if user_number == comp_number:
                print("Вы победили")
                is_run = False