k = float(input())

c = k-273.15
f = c*1.8+32

if f>212:
    print("Temperature is too high!")
else:
    #錯的
    # print(f"{c:.2f,f:.2f}",sep=" ")
    print(f"{c:.2f} {f:.2f}")
