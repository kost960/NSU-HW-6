import math
ent_quantity = input('Введите кол-во детей, сколько детей вмещает карусель и сколько длится 1 сеанс(через пробел): ')
quantity = ent_quantity.split()
time = (math.ceil((int(quantity[0])/int(quantity[1])))*int(quantity[2])*2)
print(time)