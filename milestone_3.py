## Package import
import random

## Create a list containing the names of your 5 favourite fruits
word_list = ["pineapple", "banana", "strawberry", "grapes", "orange"]
print(word_list)

## Word randomiser
word = random.choice(word_list)
print(word)


answer_validity = True
## While loop with the condition as True
while answer_validity == True:
    guess = input("Please enter a letter")
    if len(guess) == 1 and guess.isalpha() == True:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical characcter.")

## If statement checking if guess is included in the word
if guess in word:
    print(f"good guess! {guess} is in the word")
else:
    print(f"Sorry, {guess} is not in the word. Please try again.")