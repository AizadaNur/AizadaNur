import math
a = int(input())
array = list(map(int, input().split()))
i=a-1

while i>=0:
    print(array[i],end=' ')
    i-=1