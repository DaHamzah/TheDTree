import random
print("Hello, what's your name?")
ParticipantName=input()

num = random.randint(1, 10)
print("well, " +ParticipantName+  ", I challenge you to find the number i am thinking about, i'll make it easy for you, it's between 1 and 10 ")
print("you have 3 tries")

guesstaken = 0

while guesstaken < 3:
    print("what's your guess")
    guess = input ()
    guess = int(guess)

    guesstaken=guesstaken+1
    if guess < num:
        print("your guess is a bit low,try agin with a higher number")
    elif guess > num:
        print("your guess is a bit high, try agin with a lower number")
    elif guess == num:
        break
if guesstaken != num:
   num = str(num)
   print("sorry you couldn't find the right number, it was" + num + "")
if guesstaken == num:
   num = str(num)
   print("lucky bastard," +num+ " is the correct number i bet you can't find the  next number")
print("would you like to try again? ")
