import random
while True:
 
 ask = input("Should We start the game of Guess The number? (y/n): ").lower()
 if ask == 'y':

     user = int(input("Enter ur Guess: "))
     guess = random.randint(1,101)
     if user == guess:
      print("Congarts Ur Guess is right!")
     else:
      print(f"Ohh Wrong Answer! The answer is {guess}")
 elif ask == 'n':
   print("Thank u!!!!")
   break
 else:
   print("Invaild Input")
  
