num_float = 3.4

if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Отрицательное число')


def study(year):
    if year <= 4:
        print('Бакалавр')
    elif year in range(5, 6):
        print('Магистр')
    elif year in range(7, 8, 9):
        print('Аспирант')
    else:
        print('Введите корректный год обучения')

study(4)

