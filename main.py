import sys
import math
import os
import time
check = False
while(True):                                                                                                                                                            #Цикл While(True) нужен для того, чтобы пользователь вышел из программы сам, тогда, когда он захочет
    print("Выберите то, что вы хотите сделать:"                                                                                                                         #Задание базового интерфейса калькулятора
          "\n1. Совершить математическую операцию с двумя числами (сложить(+), вычесть(-), умножить(*), делить(/))"
          "\n2. Совершить математическую операцию с одним числом (возвести в степень ЦЕЛОГО ЧИСЛА(^), взять квадратный корень (sqrt), факториал числа(!))"
          "\n3. Решить квадратное уравнение по заданным коэффициентам a, b, c"
          "\n4. Выход"
          "\nВаш выбор: ", end="")
    inp = input()                                                              #Выбор опции, осуществляется через if и elif
    if (inp == "1"):                                                           #Опция №1
        os.system('cls')                                                       #Очищение консоли для более удобного использования
        while(True):                                                           #Проверка вводимых String данных, будет ещё несколько раз встречаться в коде
            symb = input("Знак (+,-,*,/): ")
            if symb in ('+', '-', '*', '/'):
                break
            else:
                print("\nНеправильный ввод, попробуйте ещё раз")
        while (check!=True):                                                   #Проверка вводимых Float данных, будет ещё несколько раз встречаться в коде
            try:
                check = True
                first = float(input("Первое число: "))
            except:
                check = False
                print("\nНеправильный ввод, попробуйте ещё раз\n")
        check = False
        while (check != True):
            try:
                check = True
                second = float(input("Второе число: "))
            except:
                check = False
                print("\nНеправильный ввод, попробуйте ещё раз\n")
        check = False

        if (symb == "+"):                                                       #Вывод результата Опции №1
            result = first + second
            print(f"\nРезультат: {result}\n")
        elif (symb == "-"):
            result = first - second
            print(f"\nРезультат: {result}\n")
        elif (symb == "*"):
            result = first * second
            print(f"\nРезультат: {result}\n")
        elif (symb == "/"):
            if (second == 0):
                print("\nДеление на 0 невозможно!\n")
            else:
                result = first / second
                print(f"\nРезультат: {result}\n")
        time.sleep(5)
        os.system('cls')

    elif (inp == "2"):                                                          #Опция №2
        os.system('cls')

        while (True):
            symb = input("Операция (^,sqrt,!): ")
            if symb in ('^', 'sqrt', '!'):
                if (symb == "^"):
                    while (check != True):
                        try:
                            check = True
                            pw = int(input("Степень: "))
                        except:
                            check = False
                            print("\nНеправильный ввод, попробуйте ещё раз\n")
                    check = False
                break
            else:
                print("\nНеправильный ввод, попробуйте ещё раз")

        while (check != True):
            try:
                check = True
                num = float(input("Число: "))
            except:
                check = False
                print("\nНеправильный ввод, попробуйте ещё раз\n")
        check = False

        if (symb == "^"):                                                       #Вывод результата Опции №2
            result = math.pow(num, pw)
            print(f"\nРезультат: {result}\n")
        if (symb == "!"):
            result = math.factorial(num)
            print(f"\nРезультат: {result}\n")
        if (symb == "sqrt"):
            result = math.sqrt(num)
            print(f"\nРезультат: {result}\n")
        time.sleep(5)
        os.system('cls')

    elif (inp == "3"):                                                          #Опция №3
        os.system('cls')

        while (check!=True):
            try:
                check = True
                a = float(input("Коэффициент a: "))
            except:
                check = False
                print("\nНеправильный ввод, попробуйте ещё раз\n")
        check = False

        while (check!=True):
            try:
                check = True
                b = float(input("Коэффициент b: "))
            except:
                check = False
                print("\nНеправильный ввод, попробуйте ещё раз\n")
        check = False

        while (check!=True):
            try:
                check = True
                c = float(input("Коэффициент c: "))
            except:
                check = False
                print("\nНеправильный ввод, попробуйте ещё раз\n")
        check = False

        d = math.pow(b, 2) - 4 * a * c                                              #Формула дискриминанта, Вывод результата Опции №3
        print(f"\nДискриминант = {d}\n")

        if (d > 0):
            x1 = (-b + math.sqrt(d)) / (2 * a)
            x2 = (-b - math.sqrt(d)) / (2 * a)
            print(f"Решение:"
                  f"\nX1: {x1}"
                  f"\nX2: {x2}\n")
        elif (d == 0):
            x = -b / (2 * a)
            print(f"Решение: {x}\n")
        else:
            print("Корней нет\n")
        time.sleep(5)
        os.system('cls')

    elif (inp == "4"):                                                              #Опция №4
        sys.exit()

    else:
        print("\nНеправильный ввод, попробуйте ещё раз\n")
        time.sleep(1)
        os.system('cls')