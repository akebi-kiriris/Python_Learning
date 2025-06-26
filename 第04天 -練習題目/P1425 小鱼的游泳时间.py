start_hour,start_min,end_hour,end_min = map(int,input().split())


if end_min>start_min:
    hour = end_hour - start_hour
    min = end_min - start_min
else:
    hour = end_hour - start_hour - 1 
    min = end_min - start_min +60
    
print(hour,min)
    
#討論區精簡版
# h1, m1, h2, m2 = map(int, input().split())
# timeh = h2 - (h1 + 1)
# timem = m2 + (60 - m1)
# if timem >= 60:
#     timem -= 60
#     timeh += 1
# print(timeh, timem)