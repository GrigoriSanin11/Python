n = int(input("wsfwefwe "))

r = 0
o = 0

for i in range(n):
    t = int(input())
    if t > 0:
        r += 1 
    else:
        o += 1
if r > o:
    print(o)
else:
    print(r)