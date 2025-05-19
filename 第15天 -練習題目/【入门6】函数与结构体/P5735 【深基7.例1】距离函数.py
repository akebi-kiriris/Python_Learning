arr = [tuple(map(float, input().split())) for i in range(3)]
dis = 0

dis += ((arr[1][0]-arr[0][0])**2 + (arr[1][1]-arr[0][1])**2)**0.5  
dis += ((arr[2][0]-arr[1][0])**2 + (arr[2][1]-arr[1][1])**2)**0.5  
dis += ((arr[0][0]-arr[2][0])**2 + (arr[0][1]-arr[2][1])**2)**0.5 

print(f"{dis:.2f}")