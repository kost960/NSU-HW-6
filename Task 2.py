hole_input = input('Введите размер отверстия: ')

brick_input = input('Введите размер кирпича: ')

hole = hole_input.split('x')

brick = brick_input.split('x')

if int(brick[0]) < int(brick[1]):
    if int(brick[1]) < int(brick[2]):
        if int(brick[0]) * int(brick[1]) > int(hole[0]) * int(hole[1]):
            print('Нет')
        else:
            print('Да')
    elif int(brick[0]) * int(brick[2]) > int(hole[0]) * int(hole[1]):
        print('Нет')
    else:
        print('Да')
elif int(brick[2]) < int(brick[0]):
    if int(brick[2]) * int(brick[1]) > int(hole[0]) * int(hole[1]):
        print('Нет')
    else:
        print('Да')
elif int(brick[0]) * int(brick[1]) > int(hole[0]) * int(hole[1]):
    print('Нет')
else:
    print('Да')
