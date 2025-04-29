n = int(input())
a = 1 #正方形的
b = 1 #三角形的數字
c = 1 #三角形的一層數字量
for i in range(n):
    for k in range(n):
        print(f"{a:02}",end='')
        a+=1
    print('')
print('')

for i in range(n):
    print(' '*(n-i-1)*2,end='')
    for k in range(c):
        print(f"{b:02}",end='')
        b+=1
    print('')
    c+=1
        