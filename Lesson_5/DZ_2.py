def sum(A, B):
    if (B==0):
        return A
    else: 
        return sum(A+1,B-1)

a = int(input('Input A>>'))
print()
b = int(input('Input B>>'))
print()
if (a>=b):
    print (sum(a,b))
else:
    print(sum(b,a))