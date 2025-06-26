n = int(input())
str_n = str(n)

if n<0:
    str_n = list(reversed(str_n))
    del str_n[len(str_n)-1]
    while str_n[0]=="0":
        del str_n[0]
    str_n.insert(0,"-")
    str_n = int(''.join(str_n))
elif n==0:
    str_n=0
else:
    str_n = list(reversed(str_n))
    while str_n[0]=="0":
        del str_n[0]
    str_n = int(''.join(str_n))

print(str_n)

#陣列操作

#deepseek解
# n = int(input())

# if n == 0:
#     print(0)
# else:
#     is_negative = n < 0
#     str_n = str(abs(n))              # 統一處理絕對值
#     str_n = list(reversed(str_n))    # 倒轉並轉成 list

#     while str_n and str_n[0] == "0":  # 移除前導 0
#         del str_n[0]

#     if is_negative:
#         str_n.insert(0, "-")         # 負號插回來

#     print(int(''.join(str_n)))