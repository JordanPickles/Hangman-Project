import random # Imports random module to be used when selecting the word for each game

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