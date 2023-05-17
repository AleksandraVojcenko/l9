number = int(input('Введите число'))
print()
if number % 3 == 0:
    print(number, 'число делится')
else:
    print('число не делится')

def p5():
    try:
        n = int(input('Введите число:'))
        g = 100 / n
    except ZeroDivisionError:
        print('Ввели ноль')
    except ValueError:
        print('Вы ввели не число')
    else:
        print('Результат: ', g)

def p6():
    date = input('Введите дату для проверки ее magicовски дд.мм.гг')
    date = date.split ('.')
    if int(date[0]) * int(date[1]) == int(date[2][2:4]):
        print('Дата magic *0*')
    else:
        print('Дата не magic')

def p7():
    happy = [int(i) for i in int(input('Введите число на проверку его счастливости :)'))]
    if sum(happy[:(happy % 2)] == sum(happy[(happy % 2):])):
        print('happy')
    else:
        print('not happy')

p5()
p6()
p7()






