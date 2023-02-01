n = input('Кол-во км за 1 день: ')
m = input('растояние: ')
n = int(n)
m = int(m)
d =  m / n  

import math

print('количество дней что бы проехать "m" расстояние: ')
print(math.ceil(d))
