n = int(input("ddtdrzdf   "  ))

max = 0
min = 1000000000000000000

for i in range(n):
    temp = int(input())
    if temp > max:
        max = temp
    if temp < min:
        min = temp
print(min, max)