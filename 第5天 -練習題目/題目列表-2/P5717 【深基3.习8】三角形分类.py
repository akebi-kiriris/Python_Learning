arr = list(map(int,input().split()))
arr = sorted(arr)
check = 1
if arr[2]>=arr[0]+arr[1]:
    print("Not triangle")
    check =0
if arr[0]**2 + arr[1]**2 == arr[2]**2 and check == 1:
    print("Right triangle")
if arr[0]**2 + arr[1]**2 > arr[2]**2 and check == 1:
    print("Acute triangle")
if arr[0]**2 + arr[1]**2 < arr[2]**2 and check == 1:
    print("Obtuse triangle")
if (arr[0]==arr[1] or arr[2]==arr[1]) and check == 1:
    print("Isosceles triangle")
if arr[0]==arr[1]==arr[2] and check == 1:
    print("Equilateral triangle")