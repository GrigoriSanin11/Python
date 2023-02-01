a = int(input('1 класс: '))
b = int(input('2 класс: '))
s = int(input('3 класс: '))
a = a / 2
b = b / 2
s = s / 2

import math
print(math.ceil(a) + math.ceil(b) + math.ceil(s))