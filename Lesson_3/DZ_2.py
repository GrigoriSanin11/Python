# 2 Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка
# содержит число X
# Пример:
# 5
# 1 2 3 4 5
# 6
# -> 5


N = int(input('количество элементов в массиве '))
A = []
p = 0
p1 = 0
for i in range(1, N+1):
    A.append(i)
print(A)

X = int(input('поиск '))
for i in A:
    if X == A[0]:
        p = A[1]
        print(p)
        break
    if X == N:
        p = N - 1
        print(p)
        break
    if X > N:
        p = N
        print(p)
        break
    else:
        p = X + 1
        p1 = X - 1
        print(p,  p1)
        break
     


