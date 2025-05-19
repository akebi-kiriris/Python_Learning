def is_prime(check):
    if check<2:
        return 0
    for i in range(2,int(check**0.5)+1):
        if check%i==0:
            return 0
    return check


n = int(input())
arr = list(map(int, input().split()))
ans =[]

for i in arr:
    if is_prime(i)!=0:
        ans.append(i)
    
print(" ".join(map(str,ans)))