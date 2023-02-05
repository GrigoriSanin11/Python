n = int(input("Введите число   "))

max_d = 0
max = 0

for i in range(n):
    nam = int(input())
    if nam > 0:
        max_d = max_d + 1
        if max_d > max:
            max = max_d
    else:
        max_d = 0
print(max)
