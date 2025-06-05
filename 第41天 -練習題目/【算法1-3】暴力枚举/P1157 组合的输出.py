#位置、當前選的數字
def dfs(index,temp):
    #夠了
    if len(temp)==r:
        output.append(temp[:])
        return
    #沒了
    if index==n:
        return
    
    #加不加進陣列
    temp.append(index + 1)
    dfs(index+1,temp)
    temp.pop() 
    dfs(index+1,temp)
        


output=[]
n,r = map(int,input().split())

dfs(0,[])
for i in output:
    for k in i:
        print(f"{k:3}",end="")
    print()