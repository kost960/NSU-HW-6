xc1 = int(input('Введите координату x центра первой окружности: '))

yc1 = int(input('Введите координату y центра первой окружности: '))

r1 = int(input('Введите радиус первой окружности: '))

xc2 = int(input('Введите координату x центра второй окружности: '))

yc2 = int(input('Введите координату y центра второй окружности: '))

r2 = int(input('Введите радиус второй окружности: '))

if ((xc1 - yc1) ** 2 + (yc1 - yc2) ** 2) ** 0.5 > (r1 + r2):
    print('Окружности лежат одна вне другой, не касаясь')

elif ((xc1 - yc1) ** 2 + (yc1 - yc2) ** 2) ** 0.5 == (r1 + r2):
    print('Окружности имеют внешнее касание')

elif ((xc1 - yc1) ** 2 + (yc1 - yc2) ** 2) ** 0.5 == (r1 - r2):
    print('Окружности имеют внутреннее касание')

elif ((xc1-yc1)**2+(yc1-yc2)**2)**0.5 < (r1 + r2):
    print('Окружности имеют внешнее касание')

else:
    print('Одна лежит внутри другой, не касаясь')
