Passwd = 5867894956

while True:
 Guess = int(input("Enter the password: \n"))
 if (Guess == Passwd):
   print("Password accecpted, Access granted \n")
   break
 else :
  print("Wrong password, Try again")