# Пратика списки 5
import random
def h5():
    s = [1, 2, 3, 4, 5]
    p = input('Введите любое число')
    if p == s:
        print('Нет такого числа ')
    else:
        print('Вы угадали')


def h6():
    h = [1, 2, 3, 8, 8]
    duplicate = {str(x) for x in h if ls.count(x) > 1}
    x = lambda: print('nothing')
    y = lambda: print(''.join(duplicate))
    x() if len(duplicate) < 1 else y()
    y() if len(duplicate) < 1 else x()


def h7():
    week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье')
    weekends = int(input())
    print('Weekends:', week[:-weekends -1:-1])
    print('Week:', week[:-weekends])


def h8():

    s1 = ["Иванов", "Ионов", "Шарипова", "Черепов", "Мидин"]
    s2 = ["Карпов", "Булашева", "Смирнова", "Лебедь","Петрова"]
    while len(numbers) < 11:
        numbers.append(random.randint(0, 10))
        numbers = list(dict.fromkeys(numbers))
        s1s2 = [s1[x] for x in numbers[:5:]]
        s1s2 += [s2[x] for x in numbers[:5:]]
        s1s2 = sorted(s1s2)
        print(len(s1s2))
        print(s1s2)
        print("Иванов" in s1)
        print(s1s2.count("Иванов"))

h8()