arr = []
arr += input().split()
temp = []
pwd = ""
min = ""
number_list = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", 
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", 
    "eighteen", "nineteen", "twenty"
]

special_list = {
    "a": 1,
    "both": 2,
    "another": 1,
    "first": 1,
    "second": 2,
    "third": 3
}

temp = []
#先換成二位數字
for i in arr:
    if i in number_list and(number_list.index(i)+1)**2<100:
        temp.append(str(f"{(number_list.index(i)+1)**2:02d}"))
    elif i in number_list and(number_list.index(i)+1)**2>=100:
        temp.append(str(f"{(number_list.index(i)+1)**2-100:02d}"))
    elif i in special_list:
        num = special_list[i]
        temp.append(str(f"{(num*num)%100:02d}"))
        
#把左側的0清掉，若全沒了則輸出0
temp = sorted(temp,key=int)

if len(temp) != 0:
    pwd = ''.join(temp).lstrip("0")
    if pwd == "":
        pwd = "0"
else:
    pwd = "0"
print(pwd)
