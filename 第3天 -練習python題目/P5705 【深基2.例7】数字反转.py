a = input()
lent = len(a)
ans = ['']*lent

for i in range(len(a)):
    ans[lent-1] = a[i]
    lent-=1
reversed_a = ''.join(ans)
print(float(reversed_a))