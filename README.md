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

## Milestone 4
This milestone developed the code into a class which inncludes the check_guess() and ask_for_input functiions. There have been further developemnts to the aforementioned functions to improve functionality of the game. The comments within the code has also been updated.

- The Hangman class is defined with the arguments and parameters defined. The class constructor uses the __init__ magic command to include the user input as one of the arugments in the class.
- The check_guess() function has been updated to add functionality to the game dependent on whether the guess is correct or not. To do this a for loop is added to the already included if statement. The else statement now includes removing the life (already attributed 5 per game in the argument definition of the class.
- The ask_for_input function contaiins a while loop with an if condition included. The if condition cotnains all 3 of the possible outcomes from the input of the user. 
- The class is then initialised and the method called at the end of this code block.

```
import random # Imports random module to be used when selecting the word for each game.

class Hangman:

    def __init__(self, word_list, num_lives): #Initialises the class, passing word_list and num_lives as the arguments
        self.word_list = word_list 
        self.num_lives = num_lives 
    
    # Defines the attributes required in the game
        self.word = random.choice(word_list) # Chooses word at random from the list
        self.word_guessed = len(self.word)*["_"] # A list of the letters to be guessed based on the length of the word
        self.num_letters = len(set(self.word) - set(self.word_guessed)) #number of unique letters still to be guessed
        self.num_lives = 5 # Number of lives is set at 5 for this game
        self.word_list = ["pineapple", "banana", "strawberry", "grapes", "orange"] # A list containing the potential words to be used in the game
        self.list_of_guesses = [] # List of previous guesses, list set to empty intiially


    def check_guess(self, guess): # This defines the function to check the users guess. Guess is passed as the arugment
        guess = guess.lower() # turns all guesses to lower case
        if guess in self.word: # Checks if the users guess is in the slected word
            print(f"good guess! {guess} is in the word")

            for i, letter in enumerate(self.word): 
                if letter == guess: #Checks if the letter guessed is in the word
                    self.word_guessed[i] = guess #Adds the guessed letter into the word

        else:
            self.num_lives -=1 #Reduces the number of lives the user has left
            print(f"Sorry, {guess} is not in the word. Try again.")
            print(f"You have {self.num_lives} lives left")
        self.list_of_guesses.extend(guess) #Adds the guess to the list of guesses to be checked during each input (see line 40)

   
    def ask_for_input(self): # Asking for input function defined with no argument
        while True: # Used to make the continuous loop which will only break if the below if statement is true 
            guess = input("Please enter a letter") # Requires an input from the user
            if len(guess) != 1 or guess.isalpha() == False: # Checks the input from the user is valid
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses: # Checks if the input has alrady been guessed by the user
                print("You already tried that letter!")            
            else:
                self.check_guess(guess) #If the guess passes through the previous conditions, guess is then checked through calling the check_guess() function

hangman = Hangman(word_list = ["pineapple", "banana", "strawberry", "grapes", "orange"], num_lives = 5) #Initiates the class
hangman.ask_for_input() # Calls the ask for input function

```
