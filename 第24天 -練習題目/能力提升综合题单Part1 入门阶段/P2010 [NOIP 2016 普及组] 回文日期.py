arr = [input().strip() for _ in range(2)]
start_date = arr[0]  
end_date = arr[1]   
check = 0

month_days = {
    1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
    7:31, 8:31, 9:30, 10:31, 11:30, 12:31
}


start_year = int(start_date[:4])
end_year = int(end_date[:4])

for year in range(start_year, end_year + 1):
    reversed_part = str(year).zfill(4)[::-1]
    pal_date = str(year) + reversed_part
    
    if not (start_date <= pal_date <= end_date):
        continue

    month = int(reversed_part[:2])
    day = int(reversed_part[2:4])
    
    if month < 1 or month > 12:
        continue
    
    max_day = month_days[month]
    
    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            max_day = 29
    if day >= 1 and day <= max_day:
        check += 1

print(check)