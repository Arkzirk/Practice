print('Общество в начале XXI века')
x = int(input('Сколько Вам лет?'))
def myfunc(x):
    if x >= 0 and x <= 7:
        t = 'Вам в детский сад'
    elif x > 7 and x <= 18:
        t = 'Вам в школу'
    elif x > 18 and x <= 25:
        t = 'Вам в профессиональное учебное заведение'
    elif x > 25 and x <= 60:
        t = 'Вам на работу'
    elif x > 60 and x <= 120:
        t = 'У вас есть выбор'
    else:
        i = 0
        while i < 5:
            print('Ошибка! Это программа для людей!')
            i = i + 1
    return t
print(myfunc(x))