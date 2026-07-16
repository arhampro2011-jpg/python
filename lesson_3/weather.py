import datetime 
import calendar
import keyword

city=input("enter your city name")
temp=float(input("what is the temperature"))
if temp>35:
    print("it is very hot today")

if temp>25:
    print("it is great to go outside")
else:
    print("carry a jacket")

if temp>35:
    print("it is very hot today")
elif temp>25:
    print("its not very hot")
else:
    print("its cold")

date_today=datetime.datetime.now()
print(date_today)

calendar_26= calendar.calendar(date_today.year)
print(calendar_26)

print(keyword.kwlist)