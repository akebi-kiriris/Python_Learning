x=int(input())
n=int(input()) 
temp = n

while temp>7:
    temp-=7

if temp+x<=7:
    print(temp+x)
else:
    print(temp+x-7)