letter = 'abcdefgh'.index(input("Введите букву: ")) + 1
number = int(input("Введите цифру: "))
if (number+letter) % 2 == 1:
    print('Белая')
else:
    print('Черная')