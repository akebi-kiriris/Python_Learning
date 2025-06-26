a,b,c = map(float,input().split(' '))

p = (a+b+c)/2
sum = (p*(p-a)*(p-b)*(p-c))**0.5
print(f"{sum:.1f}")

#注意不能用int
