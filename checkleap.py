def CheckLeap(Year):

  if ((Year % 400 == 0) or
   (Year % 100 != 0) and
   (Year % 4 == 0)):
    print("leap Year")

  else:
    print("not a leap Year")


print(CheckLeap(2020))
