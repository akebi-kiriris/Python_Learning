#2 (2出現1次)
# 2 3  #(2出現2次)
# 23 2 3
# 2 3 6 
# 2 3 6 23 26 36 (2出現4次)
arr = list(map(int,input().split()))
print(sum(arr)*2**(len(arr)-1))