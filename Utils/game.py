#Import the random module
import random

class Hangman: 
    # Attributes needed: possible_words, word_to_find, lives, correctly_guessed_letters

    # Create the world list
    possible_words = ['becode', 'learning', 'mathematics', 'sessions']

    # Initialize the object with the needed attributes
    def __init__ (self):
        # Select a random word from the list
        self.word_to_find = random.choice(Hangman.possible_words)
        self.lives = 5
        self.correctly_guessed_letters = ("_ " * len(self.word_to_find)).rstrip()
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0

    # Play one round of Hangman
    def play (self):
        # Making sure the player_guess var is empty
        player_guess = ""
        #ASking the player for a letter
        player_guess = input("Please guess a letter")
        #Veryfying the input is 1 character and part of the alphabet
        while (len(player_guess) != 1) or (player_guess.isalpha() == False):
            player_guess = input("That was not 1 letter, please enter a single letter")
        # If the player guessed correctly
        if player_guess in self.word_to_find:
            print(f"Congratulations, you guessed {player_guess} correctly!")
            # Looking for the index(es) of the guessed letter 
            positions = [pos for pos, char in enumerate(self.word_to_find) if char == player_guess]
            # Updating the correctly_guessed_letters attribute
            for pos in positions:
                i = pos * 2
                self.correctly_guessed_letters = self.correctly_guessed_letters[:i] + player_guess + self.correctly_guessed_letters[i + 1:]

        # If the player guessed wrong
        else:
            print("Sorry, that letter is not part of the word!")
            # Check if the letter is already in the list
            if player_guess not in self.wrongly_guessed_letters:
                # Adding the letter to the wrong letter list
                self.wrongly_guessed_letters += player_guess
            self.error_count += 1
            self.lives -= 1

    # Play a game of hangman
    def start_game (self):
        # Keep playing until one of the finish criteria are met
        while True:
            self.play()
            self.turn_count += 1
            # Game over if lives are at 0
            if self.lives == 0:
                self.game_over()
            # Victory if all letters are found
            if "_" not in self.correctly_guessed_letters: 
                self.well_played()
            # Printing results of this round
            print("Letters you have found so far:", self.correctly_guessed_letters)
            print("Letters you have guessed wrong:", sorted(self.wrongly_guessed_letters))
            print(f"You have {self.lives} lives remaining.")
            print(f"You have made {self.error_count} mistakes.")
            print(f"You have been playing for {self.turn_count} rounds.")                


    # Game over
    def game_over (self):
        print("game over...")
        exit()

    # Victory
    def well_played (self):
        print(f"You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!")
        exit()
