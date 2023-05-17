def p1():
    n = int(input())
    s = ''

    for i in range(1, n + 1):
        word = input()
        s = s + word + ' '
        word = ''

    print(s)


def p2():
    s = ''
    word = input()

    while word != 'stop':
        s = s + word + ' '
        word = input()
    print(s)

def p3():
    word = input("введите слово:")
    for i in word:
        if i == "Ф" or i == "ф":
            print("Слово редкое")
            break
        else:
            print("Слово обычное")
            break

def p4():
    import random
    print('Для завершение напишите - stop')
    kn = 0
    k = 0
    while (k!=3):
        while True:
            a = random.randint(1, 20)
            b = random.randint(1, 20)
            print(f"{a} + {b}=", end="")
            res = input()
            while not res.isdigit() and res != "stop":
                print('Ввод неверен, попробуйте ещё раз', end="")
                res = input()
            if res == 'stop':
                break
            res = int(res)
            if a+b == res:
                k += 1
                print('Ответ верен')
            else:
                print("Ответ ошибочен:(")
                kn+=1
            if kn == 3:
                print("Игра окончена. Правильных ответов:", k)

