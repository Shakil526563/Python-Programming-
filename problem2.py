import random
for x in range(1,6):
   guessnumber=int(input("Enter your guess number 1 to 5 :"))
   randomnumber=random.randint(1,5)

   if guessnumber==randomnumber:
      print("you are win")
   else:
     print("you are loss")
     print("random was ",randomnumber)
