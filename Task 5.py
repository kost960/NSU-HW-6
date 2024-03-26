ent_way = input('Введите путь: ')
way = ent_way.split('-')
x1 = 'abcdefgh'.index(way[0][0]) + 1
y1 = int(way[0][1])
x2 = 'abcdefgh'.index(way[1][0]) + 1
y2 = int(way[1][1])

if (x1-x2 == 1 or x1-x2 == -1) and (y1-y2 == 2 or y1-y2 == -2):
    print('Верно')
elif (x1-x2 == 2 or x1-x2 == -2) and (y1-y2 == 1 or y1-y2 == -1):
    print('Верно')
else:
    print('Неверно')