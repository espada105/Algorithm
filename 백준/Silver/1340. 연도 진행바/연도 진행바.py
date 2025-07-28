input_data = input().split()

month_dict = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]

month = month_dict.index(input_data[0]) + 1
date = int(input_data[1][:-1])
year = int(input_data[2])
time = input_data[3]
hour, minutes = map(int, time.split(":"))

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if is_leap(year):
    days_in_month[1] = 29

total = sum(days_in_month) * 24 * 60
passed_minutes = 0

for i in range(month-1):
    passed_minutes += days_in_month[i] * 24 * 60

passed_minutes += (date - 1) * 24 * 60
passed_minutes += hour * 60 + minutes

result = passed_minutes / total * 100
print(result)