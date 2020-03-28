n=int(input())
i=1
ispoweroftwo = False

while i <= n:
    if i == n:
        ispoweroftwo=True
    i*=2

if ispoweroftwo:
    print('YES')
else:
    print('NO')