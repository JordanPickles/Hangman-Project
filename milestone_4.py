class Hangman:
    import random # Imports random module to be used when selecting the word for each game
    def __init__(self, word_list, num_lives): #Initialises the class, passing word_list and num_lives as the arguments
        self.word_list = word_list 
        self.num_lives = num_lives 
    
    # Defines the attributes required in the game
        self.word = random.choice(word_list) # Chooses word at random from the list
        self.word_guessed = [",",",",",",",",",",","] # A list of the letters to be guessed
        self.num_letters = len({self.word} - {self.word_guessed}) #number of unique letters still to be guessed
        self.num_lives = 5 # Number of lives is set at 5 for this game
        self.word_list = word_list = ["pineapple", "banana", "strawberry", "grapes", "orange"] # A list containing the potential words to be used in the game
        self.list_of_guesses = [] # List of previous guesses, list set to empty intiially


    def check_guess(self, guess): # This defines the function to check the users guess. Guess is passed as the arugment
        guess = guess.lower() # turns all guesses to lower case
        if guess in self.word: # Checks if the users guess is in the slected word
            print(f"good guess! {guess} is in the word")
        else:
            print(f"Sorry, {guess} is not in the word. Please try again.")
        
   
    def ask_for_input(guess):
        while answer_validity == True:
            guess = input("Please enter a letter")
            if len(guess) == 1 and guess.isalpha() == True:
                break
            else:
                print("Invalid letter. Please, enter a single alphabetical characcter.")
        check_guess(guess)
        ask_for_input(guess)
        