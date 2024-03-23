number = int(input('Введите число: '))

output_number = list(range(-1, 201))

if number < 10:
    print(output_number[number])
elif number < 191:
    print(str(output_number[(number-9)//2 + 10])[number % 2])
else:
    print(str(output_number[(number-188)//3 + 100])[((number - 188) % 3)])
