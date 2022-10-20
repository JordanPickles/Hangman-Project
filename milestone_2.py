## Package import
import random

## Create a list containing the names of your 5 favourite fruits
word_list = ["pineapple", "banana", "strawberry", "grapes", "orange"]
print(word_list)

## Word randomiser
word = random.choice(word_list)
print(word)

## Request input from user
guess = input("Please enter a letter")

## If statement to check the lenght of the input is 1 and the input is an alphabet
if len(guess) == 1 and guess.isalpha() == True:
    print("Good guess!")
else:
    print("Oops! That is not a valid input")
