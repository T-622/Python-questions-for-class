import random

while True:
  randint = random.randint(1,20)
  Guess = int (input("Guess the random number: \n"))

  if (randint == Guess): 

   print("You Got It! \n Thanks for playing! ")

   break

  else :

   print("Try again")
   print("The random number was: \n", randint)
   print()





