array = []
n = input()
for i in range(int(n)):
    num = input()
    array.append(int(num))
    
for i in range(int(n)):
    if i % 2 == 0:
        print(array[i], end=" ")