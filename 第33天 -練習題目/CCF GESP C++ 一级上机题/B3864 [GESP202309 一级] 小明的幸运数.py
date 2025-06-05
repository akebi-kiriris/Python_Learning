n = [int(input()) for i in range(3)]
summ = 0
for i in range(n[1],n[2]+1):
    if i%10==n[0] or i%n[0]==0:
        summ+=i

print(summ)