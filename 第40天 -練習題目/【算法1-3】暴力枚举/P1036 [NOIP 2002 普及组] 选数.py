#檢查是否為質數
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

#傳入目前的位置 index、已選的數量 count、目前總和 total
#對該位置的數字進行二分選擇--選或不選，若選了則數量+1並加上 total，繼續遞迴
#若數量夠了則檢查是否為質數，並將總和傳入is_prime函式
def dfs(index, count, total):
    global ans
    #夠了就算
    if count == k:
        if is_prime(total):
            ans += 1
        return
    #沒有數字能判斷了就結束
    if index == n:
        return

    # 選這個數字
    dfs(index + 1, count + 1, total + nums[index])
    # 不選這個數字
    dfs(index + 1, count, total)

ans = 0
n, k = map(int, input().split())
nums = list(map(int, input().split()))


dfs(0, 0, 0)
print(ans)

#這個題目是一個陣列的數字，現在寫了一個dfs函式，傳入目前的位置(index)、
#已選的數量(count)、目前的總和(total)。

#dfs為二分法，分為選或不選，一開始先檢查是否選夠了，選夠了就呼叫is_prime函式檢查是否為質數，
#再檢查是否沒數字可選了，若是則結束查詢，接著決定要不要將當前位置的數字加入使用的數字中。

#這樣不會有重複的數字，如若第一個不選，則
#  不
#選  不
#分為兩條路，由於是按照陣列的index逐漸加上去找的，因此不會回頭。

#結果會像是
#選 不 選 選
#選 選 不 選
#各自不重複