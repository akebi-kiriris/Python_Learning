parts = input().split()
w = int(parts[0])
h = float(parts[1])

if (w/h**2<18.5):
    print("Underweight")
elif (w/h**2<24):
    print("Normal")
else:
    print(f"{w/h**2:.6g}","Overweight",sep='\n')
    
#.6g代表
# g：自动选择 f（小数）或 e（科学计数法）格式。
# 6：保留6位有效数字。