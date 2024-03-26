up_left1 = list(map(float, input('Введите координаты верхней левой вершины: ').split()))

lower_rt1 = list(map(float, input('Введите координаты нижней правой вершины: ').split()))

up_left2 = list(map(float, input('Введите координаты верхней левой вершины: ').split()))

lower_rt2 = list(map(float, input('Введите координаты нижней правой вершины: ').split()))

lower_left1 = [up_left1[0], lower_rt1[1]]

up_rt1 = [up_left1[1], lower_rt1[0]]

lower_left2 = [up_left2[0], lower_rt2[1]]

up_rt2 = [up_left2[1], lower_rt2[0]]


def check_point(up_left1, lower_rt1, lower_left1, up_rt1, checked_point):
    # вне друг друга
    if (up_left1[1] < checked_point[1] or lower_left1[1] > checked_point[1] or up_rt1[0] < checked_point[0]
            or up_left1[0] > checked_point[0]):
        return 0
    # касается
    if (up_left1[0] <= checked_point[0] <= up_rt1[0] and up_rt1[1] == checked_point[1]
            or lower_left1[0] <= checked_point[0] <= lower_rt1[0] and lower_rt1[1] == checked_point[1]
            or up_rt1[1] <= checked_point[1] <= lower_rt1[1] and up_rt1[0] == checked_point[0]
            or up_left1[1] <= checked_point[1] <= lower_left1[1] and up_left1[0] == checked_point[0]):
        return 1
    # внутри
    if (up_left1[1] > checked_point[1] and lower_left1[1] < checked_point[1] and up_rt1[0] > checked_point[0]
            and up_left1[0] < checked_point[0]):
        return 2


def point_position(res):
    global point_inside_count, point_border_count
    match res:
        case 0:
            return
        case 1:
            point_border_count += 1
            return
        case 2:
            point_inside_count += 1
            return


point_inside_count = 0
point_border_count = 0
res1 = check_point(up_left1, lower_rt1, lower_left1, up_rt1, up_left2)
res2 = check_point(up_left1, lower_rt1, lower_left1, up_rt1, up_rt2)
res3 = check_point(up_left1, lower_rt1, lower_left1, up_rt1, lower_left2)
res4 = check_point(up_left1, lower_rt1, lower_left1, up_rt1, lower_rt2)

point_position(res1)
point_position(res2)
point_position(res3)
point_position(res4)

if point_inside_count == 0 and point_border_count == 0:
    print('Прямоугольники лежат вне друг друга, не касаясь')
elif point_inside_count == 4 and point_border_count == 0:
    print('Один прямоугольник лежит внутри другого, не касаясь')
elif 0 < point_border_count <= 4:
    print('Прямоугольники имеют касание')
else:
    print('Прямоугольники имеют пересечение')

