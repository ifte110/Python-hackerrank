import calendar

m, d , y = map(int,input().split())

name = calendar.day_name[calendar.weekday(y,m,d)]

print(name)