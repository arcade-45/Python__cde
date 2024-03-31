import random
import math

lower = int(input("Please enter the lower limit: ")) #range starting from
upper = int(input("Please enter the upper limit: ")) #range ending at


x = random.randint(lower, upper) #python will guess a random number
max_no_of_tries = round(math.log(abs(lower - upper) + 1, 2))
print("\nYou have only ",max_no_of_tries," tries to guess the number")
#the formula to find out the suitable amount of tries

count_answer = 0 #to count the number of tries by the user

while count_answer < max_no_of_tries:
    count_answer +=1

    guess = int(input("Enter the guessed number: "))

    if x==guess:
         print("Congrats, You have entered the right number in ", count_answer, " tries!")
         break

    elif x > guess:
         print("The value you have entered is too less! ")

    elif x < guess:
         print("The value you have entered is too big! ")

if count_answer >= max_no_of_tries:
    print("The correct number is %d" %x)
    print("Better luck next time")

