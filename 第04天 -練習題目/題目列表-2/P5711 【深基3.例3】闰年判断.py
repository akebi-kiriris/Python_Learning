year = int(input())

print(int((year/4-year//4==0 and year/100-year//100!=0) or (year/400-year//400==0)))



# deepseek改運算符
# year = int(input())
# print((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0))