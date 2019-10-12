#!/usr/bin/python3

class Game:

    def __init__(self):
        self.name = 'Guess 1234'

    def goodguess(self, guess):
        if guess is None:
            return False
        try:
            int_guess = int(guess)
        except ValueError:
            return False
        return self.verify_number(int_guess)

    def verify_number(self, int_guess):
        return int_guess == 1234

    def hint(self, guess):
        if guess is None:
            return 'Guess the number!'
        try:
            int(guess)
        except ValueError:
            return 'Enter the number'
        return 'Enter 1234 to win!'


def main():
    game = Game()
    print('Game {}'.format(game.name))
    user_guess = None
    while not game.goodguess(user_guess):
        print(game.hint(user_guess))
        user_guess = input('Another guess: ')
    print('You won')

if __name__ == "__main__":
    main()
