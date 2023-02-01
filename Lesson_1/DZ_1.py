a = int(input("число  "))

sum = 0

while a != 0:
    sum = a % 10 + sum
    a = a // 10

print(sum)