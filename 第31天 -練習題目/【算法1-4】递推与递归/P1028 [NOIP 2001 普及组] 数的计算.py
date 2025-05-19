n = int(input())
num = [0] * (n + 1)

#以n開頭的序列，先從前面的序列一步步遞推
# num[i] 表示以 i 為起點的所有合法序列的數量
for i in range(1,n+1):
    num[i]=1
    #以j為第二(最大只能到i的一半)的後續
    for j in range(1,i//2+1):
        # 把以 j 為起點的數列接在 i 後面
        num[i]+=num[j]

print(num[n])

#6
#61
#62
#63
#621
#631