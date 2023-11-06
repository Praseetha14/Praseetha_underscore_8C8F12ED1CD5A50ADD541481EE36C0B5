def isLeapYear(year):
  if(year % 4==0 and year % 100 !=0) or year % 400==0:
    return True
  else:
    return False
Year =2020
if isLeapYear(Year):
  print("{}is a leap year.".format(Year))
else:
  print("{}is not a leap year.".format(Year))