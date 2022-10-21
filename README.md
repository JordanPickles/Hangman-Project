# Hangman-Project

## Milestone 1
Within this milestone, the github repository was created. Using git commands within the bash terminal, the repostiory was clone to the terminal in VSCode to enable the desired files to be commited and pushed to the repository at regular intervals

```
(base) Jordans-MacBook-Air:Hangman jordanpickles$ git clone https://github.com/JordanPickles/Hangman-Project.git
Cloning into 'Hangman-Project'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), done.

(base) Jordans-MacBook-Air:Hangman-Project jordanpickles$ cd ..
(base) Jordans-MacBook-Air:Hangman jordanpickles$ mv milestone_2.py Hangman-Project
(base) Jordans-MacBook-Air:Hangman jordanpickles$ cd Hangman-Project
(base) Jordans-MacBook-Air:Hangman-Project jordanpickles$ ls -a
.               ..              .git            README.md       milestone_2.py
(base) Jordans-MacBook-Air:Hangman-Project jordanpickles$ git add .
(base) Jordans-MacBook-Air:Hangman-Project jordanpickles$ git commit -m "Adds milestone-2 file"
[main 1246861] Adds milestone-2 file
 Committer: Jordan Pickles <jordanpickles@Jordans-MacBook-Air.local>
Your name and email address were configured automatically based
on your username and hostname. Please check that they are accurate.
You can suppress this message by setting them explicitly. Run the
following command and follow the instructions in your editor to edit
your configuration file:

    git config --global --edit

After doing this, you may fix the identity used for this commit with:

    git commit --amend --reset-author

 1 file changed, 19 insertions(+)
 create mode 100644 milestone_2.py
(base) Jordans-MacBook-Air:Hangman-Project jordanpickles$ git push
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 2 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 612 bytes | 612.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/JordanPickles/Hangman-Project.git
   cf323a4..1246861  main -> main
(base) Jordans-MacBook-Air:Hangman-Project jordanpickles$ 
```

## Milestone 2
--
This milestone developed the basics of the project, 
With the following stages
- The words to be included in the game assigned to a variable in a list
- the random.choice function used to randomly choose the word within each game
- The input function included to require an onput (guess of a letter within the word) 
- If statement used to determine if the user input was a valid input and return a message to the user


```## Package import
import random

## Create a list containing  5 favourite fruits
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
```
## Milestone 3
This milestone developed the checking of the letter in the word. As well as incoprotating the checks as functions.
- The validity check of the input was added to a while loop to ask for another input, should the input be invalid
- The two check below were defined as functions

``` 
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
def ask_for_input(guess):
    while answer_validity == True:
        guess = input("Please enter a letter")
        if len(guess) == 1 and guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical characcter.")
    check_guess(guess)
ask_for_input(guess)

## If statement checking if guess is included in the word
def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f"good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Please try again.")
```
