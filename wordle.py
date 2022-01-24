import enchant
import re

class WordleGame():
    def __init__(self, tot_guess):
        self.total_guesses = tot_guess
        self.guesses = self.total_guesses
        self.dictionary = enchant.Dict("en_US")
    
    def start(self):
        self.get_word()
        self.get_input()

    def get_word(self):
        import random
        with open("fiveletterwords.txt", "r") as f:
            allText = f.read()
            words = list(map(str, allText.split()))
        self.word = random.choice(words).lower()

    def get_input(self):
        regex = re.compile('[^a-zA-Z]')
        while self.guesses > 0:
            player_guess = input("\nguess the word:\n> ").lower()
            player_guess_mod = regex.sub("", player_guess)
            if len(player_guess) == 5 and len(player_guess_mod) == 5 and self.dictionary.check(player_guess)==True:
                self.guess(player_guess)
            else:
                print("five letter words.")
        self.print_word()

    def guess(self, guess):
        if self.guesses > 0:
            guess_output = [0 for i in range(5)]
            self.guesses -= 1
            for i, letter in enumerate(guess):
                if self.word[i] == letter:
                    guess_output[i] = 2
                    continue
                elif letter in self.word:
                    guess_output[i] = 1
            if guess_output != [2 for i in range(5)]:
                print(f": {guess_output[0]}{guess_output[1]}{guess_output[2]}{guess_output[3]}{guess_output[4]}")
            else:
                self.end_game()

    def end_game(self):
        print(f"\nYou guessed the correct word in {self.total_guesses-self.guesses}/6 tries\n")
        self.guesses = 0

    def print_word(self):
        print(f"\nCORRECT WORD :: {self.word}\n")
        
if __name__ == "__main__":
    game = WordleGame(6)
    game.start()
    input()