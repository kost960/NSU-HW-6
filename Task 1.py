R = 6.5
rectangle = input('Введите длины сторон прямоугольника AxB: ')
sides = rectangle.split('x')
if R*2 < ((int(sides[0])**2 + int(sides[1])**2)**0.5):
    print('Нет')
else:
    print('Да')