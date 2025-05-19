# #n為人 m為最多幾套 k為最多幾天
# n,m,k = map(int,input().split())
# day = [0]*(k+1)
# arr=[]
# for i in range(n):
#     arr.append(list(map(int,input().split())))

        
# #從第一套到最後一套
# for exam in range(m):  
#     #第一天到最後一天
#     for d in range(1, k + 1):
#         check = [] #用於確認該套是否已經在當天用過
#         #從第一人到最後一人
#         for person in range(n):  
#             #若該人有在某一天考了這一套
#             if arr[person][exam] == d: 
#                 #若這一套這天還沒考過
#                 if d not in check: 
#                     day[d] += 1 #這天需要準備一套
#                     check.append(d) #這套考題這天已考過

# print(' '.join(map(str, day[1:k+1])))

#按第一套到最後一套、第一天到最後一天的方式，按人一個一個比對，若該人有在該天考了
#這一套，就要準備這一套試題，並加進check以避免重複準備，並且這一天需要準備的試題+1


#deepseek集合版解
n, m, k = map(int, input().split())
day_sets = [set() for _ in range(k+1)]  # 每天對應一個集合（1-based）

for _ in range(n):
    schedule = list(map(int, input().split()))  # 選手的模擬賽安排
    for exam_num in range(m):
        day = schedule[exam_num]  # 這個選手的第exam_num套在哪天考。exam_num為該人第幾次考的即是第幾套
        day_sets[day].add(exam_num + 1)  # 將模擬賽編號加入對應天的集合

# 統計結果：每天集合的大小就是需要準備的場次
result = [len(day_sets[d]) for d in range(1, k+1)]
print(' '.join(map(str, result)))