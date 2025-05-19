#矩陣長寬為2**n，將矩陣設為1(不被赦免)
n = int(input())
lent=2**n
arr = [[1 for i in range(lent)] for k in range(lent)]

#分四塊進行，先進行左上，並且遞迴進行其他三塊(因只有左上為0)，其他三塊需繼續找左上直到只剩1*1的區域
def cal(x,y,lent):
    if lent ==1:
        return
    #找左上(目前矩陣的長度//2)
    half = lent//2
    #將左上範圍內的都設成0
    for i in range(x,x+half):
        for k in range(y,y+half):
            arr[i][k] = 0
    #計算其他三塊，並讓他們繼續把左上設為0。
    cal(x,y+half,half)
    cal(x+half,y,half)
    cal(x+half,y+half,half)
    

cal(0,0,lent)

for row in arr:
    print(' '.join(map(str, row)))