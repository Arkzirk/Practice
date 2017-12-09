x = int(input('Введите число от 1 до 9'))
if x >= 1 and x <= 3:
    s = input('Введите строку')
    n = int(input('Сколько раз повторить строку?'))
    ex = s * n
    print(ex)
elif x >= 4 and x <= 6:
    m = int(input('В какую степень возвести число?'))
    ex2 = x ** m
    print(ex2)
elif x >= 7 and x <= 9:
    i = 0
    while i < 10:
        x = x + 1
        i = i + 1
        print(x)
else:
    print('Ошибка ввода')