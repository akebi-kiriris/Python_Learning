from math import ceil
n = int(input())
x = int(input())
y = int(input())

fin = n-ceil(y/x)
if fin==0:
    print(1)
else:
    print(fin)