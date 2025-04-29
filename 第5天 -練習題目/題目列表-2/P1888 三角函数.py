from math import gcd

arr = sorted(list(map(int,input().split())))
g = gcd(arr[0],arr[2])
if g!=1:
    arr[0]/=g
    arr[2]/=g

print("%d/%d"%(arr[0],arr[2]))

#("%d/%d"%(arr[0],arr[2]))

#deepseek解
#print(f"{arr[0]}/{arr[2]}") 