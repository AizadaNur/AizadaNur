def xor(a, b):
    return a^b
array = list(map(int, input().split()))
print(xor(array[0], array[1]))