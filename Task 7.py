def can_order_sushi(k):
    if k % 5 == 0 or k % 7 == 0:
        return True
    for i in range(1, k // 7 + 1):
        if (k - 7 * i) % 5 == 0:
            return True

    return False


if can_order_sushi(int(input('Введите кол-во суши: '))):
    print('Да')
else:
    print('Нет')
