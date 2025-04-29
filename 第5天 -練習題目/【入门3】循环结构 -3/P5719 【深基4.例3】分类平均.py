n,k = map(int,input().split())

a = n//k
sum_a = 0

for i in range(1,a+1):
    sum_a+=i*k
avg_a = f"{sum_a/a:.1f}"

sum_b = (1+n)*n/2 - sum_a
avg_b = f"{sum_b/(n-a):.1f}"

print(avg_a,avg_b)