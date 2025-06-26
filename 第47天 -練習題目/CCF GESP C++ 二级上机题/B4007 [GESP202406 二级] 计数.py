n = int(input())
k = input()
summ=0

for i in range(1,n+1):
    for temp in str(i):
        if k==temp:
            summ+=1 

print(summ)