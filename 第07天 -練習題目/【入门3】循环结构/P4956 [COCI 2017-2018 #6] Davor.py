#2025/4/23 7.19-46
from math import ceil
n = int(input())
n = ceil((n/52)/7)
x = 1
k = 1

#每周能存7x+21k，平均一天x+3k

#先檢查是否光x=100 k=1就能解決
x = 100
if x+3*k>n:
    while x+3*k>n:
        x-=1
    while x+3*k==n:
        x-=1
    x+=1
    print(x,k,sep='\n')
#若光靠x=100無法解決，從k+1慢慢上去，k最大就為100。x保持最大，K慢慢加，頂天100 100。超過後慢慢x-1
else:
    while x+3*k<n:
        k+=1
    while x+3*k>n:
        x-=1
    while x+3*k==n:
        x-=1
    x+=1
    print(x,k,sep='\n')


