def CheckLeap(Year):

  if ((Year % 400 == 0) or
   (Year % 100 != 0) and
   (Year % 4 == 0)):
    return "leap year"

  else:
    return "not a leap Year"


print(CheckLeap(2020))
