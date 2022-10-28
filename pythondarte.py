import datetime
x=datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

c=datetime.datetime(2000,3,31)
print(c)
print(x.strftime("%B"))
print(x.strftime("%S"))#second
print(x.strftime("%M"))#minutes
print(x.strftime("%p"))#AM/PM
print(x.strftime("%m"))#month
print(x.strftime("%w"))#weekday
print(x.strftime("%b"))#weekday
print(x.strftime("%a"))#day
print(x.strftime("%f"))#microsecond

print(x.strftime("%Z"))#timezone
print(x.strftime("%H"))#hrs
print(x.strftime("%I"))
print(x.strftime("%j"))#day number of year
print(x.strftime("%U"))#week number of year
print(x.strftime("%V"))#week number of year
print(x.strftime("%G"))#year
print(x.strftime("%Z"))
print(x.strftime("%z"))