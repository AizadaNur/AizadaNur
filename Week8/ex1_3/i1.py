import math

x=int(input())
sum=0

for i in range(1, int(math.sqrt(x))):
    if(x%i==0):
        sum+=1

if (x%math.sqrt(x)==0):
    print(sum * 2 + 1)
else :
    print(sum * 2)