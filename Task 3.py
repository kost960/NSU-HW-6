square = input('Введите: ')
k = int(input('Введите K:'))
square2 = list(map(int, square.split('x')))
if k % square2[0] == 0 or k % square2[1] == 0:
    print('Yes')
else:
    print('No')
