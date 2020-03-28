import math
a = int(input())
array = list(map(int, input().split()))
cnt = 0
i=1
while i<a:
    if array[i]> array[i-1]:
        cnt=cnt+1
    i += 1
print(cnt)  