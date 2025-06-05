n = int(input())

summ=0

for i in range(1,int(n**0.5)+1):
    if n%i==0:
        summ+=1

print(summ)