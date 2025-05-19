def checkab(a, b):
    if a == 0:  
        if b == 0: return 0
        elif b == 2 or b == 3: return 1  
        elif b == 1 or b == 4: return -1
    elif a == 1: 
        if b == 1: return 0
        elif b == 0 or b == 3: return 1  
        elif b == 2 or b == 4: return -1
    elif a == 2: 
        if b == 2: return 0
        elif b == 1 or b == 4: return 1 
        elif b == 0 or b == 3: return -1
    elif a == 3:  
        if b == 3: return 0
        elif b == 2 or b == 4: return 1 
        elif b == 0 or b == 1: return -1
    elif a == 4:  
        if b == 4: return 0
        elif b == 0 or b == 1: return 1  
        elif b == 2 or b == 3: return -1

n, a_len, b_len = map(int, input().split())
a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))
pos_a = 0
pos_b = 0
score_a = 0
score_b = 0

for _ in range(n):
    res = checkab(a_arr[pos_a], b_arr[pos_b])
    if res == 1:
        score_a += 1
    elif res == -1:
        score_b += 1
    
    pos_a = (pos_a + 1) % a_len
    pos_b = (pos_b + 1) % b_len

print(score_a, score_b)

# #gpt優化
# # 勝利關係表，key 打敗 value 中的所有手勢
# win_table = {
#     0: [2, 3],  # 剪刀 > 布、蜥蜴人
#     1: [0, 3],  # 石頭 > 剪刀、蜥蜴人
#     2: [1, 4],  # 布 > 石頭、Spock
#     3: [2, 4],  # 蜥蜴人 > 布、Spock
#     4: [0, 1]   # Spock > 剪刀、石頭
# }

# def checkab(a, b):
#     if a == b:
#         return 0
#     elif b in win_table[a]:
#         return 1
#     else:
#         return -1

# #deepseek解
# n, a_len, b_len = map(int, input().split())
# a_sequence = list(map(int, input().split()))
# b_sequence = list(map(int, input().split()))

# # 胜负关系表：result[a][b]表示a对b的结果
# # 1表示a赢，0表示平局，-1表示a输
# result = [
#     [0, -1, 1, 1, -1],   # 剪刀(0)
#     [1, 0, -1, 1, -1],    # 石头(1)
#     [-1, 1, 0, -1, 1],    # 布(2)
#     [-1, -1, 1, 0, 1],    # 蜥蜴人(3)
#     [1, 1, -1, -1, 0]     # 斯波克(4)
# ]

# a_score = 0
# b_score = 0

# for i in range(n):
#     a_move = a_sequence[i % a_len]
#     b_move = b_sequence[i % b_len]
    
#     if result[a_move][b_move] == 1:
#         a_score += 1
#     elif result[a_move][b_move] == -1:
#         b_score += 1

# print(a_score, b_score)