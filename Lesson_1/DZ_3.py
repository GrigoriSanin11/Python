a = int(input('введите 6 значное число: '))

b = a % 1000
s = a // 1000
sum = 0
sum1 = 0

while b !=0:
    sum = b % 10 + sum
    b = b // 10
    sum1 = s % 10 + sum1
    s = s // 10
if sum == sum1:
    print('yes')
else: 
    print('no')

