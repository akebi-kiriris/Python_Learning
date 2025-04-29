n = int(input())
f = 1       #前一個階乘
sum = 0     #總和

for i in range(1,n+1):
    f*=i
    sum +=f

print(sum)
