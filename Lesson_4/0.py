string = input().split()
for i in range(len(string)):
    count = 1
    for j in range(i + 1, len(string)):
        if string[i] == string[j]:
            string[j] += "_" + str(count)
            count += 1

print(*string)

string = input().split()

d = {}.fromkeys(string, 0)