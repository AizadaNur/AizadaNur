import math
a = int(input())
array = list(map(int, input().split()))
cnt = 0
check=False
i=1
while i<a:
    if (array[i]>0 and array[i-1]>0) or (array[i]<=0 and array[i-1]<=0):
        check=True
    i=i+1


if (check):
    print('YES')
else:
    print('NO')
