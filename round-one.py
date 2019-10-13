#!/usr/bin/python3

class Game:

    def __init__(self):
        self.name = 'Odd/even game'
        self.odds = 3

    def goodguess(self, guess):
        if guess is None:
            return False
        try:
            int_guess = int(guess)
        except ValueError:
            return False
        return self.verify_number(int_guess)

    def verify_number(self, int_guess):
        return self.count_odds(int_guess) == self.odds

    def hint(self, guess):
        if guess is None:
            return 'Guess the number!'
        try:
            int_guess = int(guess)
        except ValueError:
            return 'Enter the number'
        if self.count_odds(int_guess) < self.odds:
            return 'Too few odds'
        elif self.count_odds(int_guess) > self.odds:
            return 'Too many odds'
        else:
            return 'You won!'

    def count_odds(self, number):
        if number == 0:
            return 1
        odds = 0
        while number != 0:
            digit = number % 10
            if digit % 2 == 0:
                odds += 1
            number //= 10
        return odds


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
