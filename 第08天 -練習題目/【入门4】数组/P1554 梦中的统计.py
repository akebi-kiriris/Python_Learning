#部分超時
# m,n = map(int,input().split())
# s = ''

# for i in range(m,n+1):
#     s+=str(i)

# for i in range(10):
#     print(s.count(str(i)),end=' ')

#改為比對
m,n = map(int,input().split())
c=[0]*10

for i in range(m,n+1):
    for k in str(i):
        c[int(k)]+=1
        

print(' '.join(map(str,c)),end=' ')
