arr =[input() for i in range(2)]
sum_t =1
sum_m =1


for i in arr[0]:
    sum_m*=ord(i)-ord("A")+1
  

for i in arr[1]:
    sum_t*=ord(i)-ord("A")+1


if sum_m%47 ==sum_t%47:
    print("GO")
else:
    print("STAY")