def fact(a,b):
    sum = 1
    for i in range(2,a+1):
        sum*=i
    sum = str(sum)
    return sum.count(str(b))



t = int(input())
arr = []
for i in range(t):
    a,b = map(int,input().split())
    arr.append(fact(a,b))

for i in arr:
    print(i)

