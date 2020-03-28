def power(a, b):
    return  pow(a, b)
array = list(map(float, input().split()))
print(power(array[0], array[1]))