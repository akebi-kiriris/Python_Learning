n = int(input())
#這樣會變二維陣列!
#arr = [input().split()]
arr = list(map(int, input().split()))

sum=0
for s in arr:
    if s%9==0 and s%8!=0:
        sum+=1
else:
    print(sum)