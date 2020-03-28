import math
a = int(input())
array = list(map(int, input().split()))
cnt = 0
i=2
while i<a:
    if array[i] <array[i-1] and array[i-1]>array[i-2]:
        cnt=cnt+1
    i += 1
print(cnt)