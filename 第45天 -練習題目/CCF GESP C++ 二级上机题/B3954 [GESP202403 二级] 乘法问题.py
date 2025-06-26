n = int(input())
temp = 1

for i in range(n):
    temp*=int(input())

if temp>1000000:
    print(">1000000")
else:
    print(temp)
    
