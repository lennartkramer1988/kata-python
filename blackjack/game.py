from blackjack.chips import Chips
from blackjack.deck import Deck
from blackjack.hand import Hand

playing = True


def game():
    while True:
        # Print an opening statement
        print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n'
              'Dealer hits until she reaches 17. Aces count as 1 or 11.')

        # Game Logic

        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")

        if new_game[0].lower() == 'y':
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break


def take_bet(chips):
    print("Not yet implemented")


def hit(deck, hand):
    print("Not yet implemented")


def hit_or_stand(deck, hand):
    print("Not yet implemented")


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


if __name__ == '__main__':
    game()
