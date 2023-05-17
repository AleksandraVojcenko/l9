def l1():
    try:
        a = int(input('Введите число '))
        b = a % 3
    except ValueError:
        print('Введено не число')
    else:
        if b == 0 and a != 0:
            print('Число делится на 3')
        elif a == 0:
            print('Введен ноль')
        else:
            print('Число не делится на 3')

def l2():
    try:
        a = int(input('Введите число '))
        b = 100/a
    except ValueError:
        print('Введено не число')
    except ZeroDivisionError:
        print('Введен 0')
    else:
        print('Результат деления 100 на введенное число')

def l3():
    date = input('Введите дату в формате дд.мм.гг: ')
    date = date.split(('.'))
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print('Дата магическая!')
    else:
        print('Дата не магическая!((((')

def l4():
    s = input('')
    if len(s) % 2 == 0:
        r1 = 0
        r2 = 0
        for i in range(len(s) // 2):
            r1 += int(s[i])
            r2 += int(s[len(s) // 2 + i])
        if r1 == r2:
            print(r1, r2, 'билет счастливый')
        else:
            print(r1, r2, 'билет не счастливый')
    else:
        print('введено не четное кол-во символов')