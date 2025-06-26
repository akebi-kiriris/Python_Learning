h,r = map(int,input().split())

pi = 3.14 
v = h * r**2*pi
v = v/1000
if ((20/v)-(20//v))!=0:
    num = 20//v+1
else:
    num = 20//v

print(int(num))

#討論區精簡版
# from math import ceil
# a,b=input().split();
# a=int(a);b=int(b);
# print(ceil(20000/(3.14*a*b*b)));