n = int(input("Ввод "))
a = 0
b = 1
c = 0
d = 2

while n > c :
    c = a + b
    a = b
    b = c
    d = d + 1

if n == c:
    print(d)
else: 
    print("-1") 
