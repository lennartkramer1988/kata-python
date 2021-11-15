# kata-python

# Verify if you have python 3 installed

You can try both `python --version` or `python3 --version`

## Download and Install python 3

1. You can find a [Python 3.10](https://www.python.org/downloads/release/python-3100/) download suitable for your system.
2. Using homebrew on a MacOS system `brew install python`

## Install the python package manager pip
This is the package manager used for python (like maven or gradle)
1.  `python3 -m pip install -U --force-reinstall pip`

# Setting up virtual environment and installing dependencies

To prevent packages / project dependencies from being installed for all your projects a virtual environment is required.
This virtual environment is a fresh python install with no other libraries installed. 
This helps prevent version conflicts between your projects (project A might use version 1 and project B might use version 2 of the same library)

## Steps

1. Install virtualenv with the pip package manager `pip install virtualenv`
2. verify your installation `virtualenv --version`
3. Go to the project root `cd kata-python`
4. Create the virtual environment `virtualenv venv` (the name venv can be anything however it is common practice to use venv)
5. Switch to the virtual environment `source venv/bin/activate`
6. Install all packages in the requirements.txt file `python3 -m pip install -r requirements.txt`



# Python basics cheat sheet





# The Kata - Object Oriented

In this kata project you will be creating a Complete BlackJack Card Game in Python.

Here are the requirements:

* You need to create a simple text-based [BlackJack](https://en.wikipedia.org/wiki/Blackjack) game
* The game needs to have one player versus an automated dealer.
* The player can stand or hit.
* The player must be able to pick their betting amount.
* You need to keep track of the player's total money.
* You need to alert the player of wins, losses, or busts, etc...

And most importantly:

* **You must use OOP and classes in some portion of your game. You can not just use functions in your game. Use classes to help you define the Deck and the Player's hand. There are many right ways to do this, so explore it well!**

Feel free to expand this game. Try including multiple players. Try adding in Double-Down and card splits! Remember to you are free to use any resources you want.

https://nl.wikipedia.org/wiki/Blackjack

## Game Play

To play a hand of Blackjack the following steps must be followed:

1. Create a deck of 52 cards
2. Shuffle the deck
3. Ask the Player for their bet
4. Make sure that the Player's bet does not exceed their available chips
5. Deal two cards to the Dealer and two cards to the Player
6. Show only one of the Dealer's cards, the other remains hidden
7. Show both of the Player's cards
8. Ask the Player if they wish to Hit, and take another card
9. If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10. If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17
11. Determine the winner and adjust the Player's chips accordingly
12. Ask the Player if they'd like to play again

## Class Definitions
Consider making a Card class where each Card object has a suit and a rank, then a Deck class to hold all 52 Card objects, and can be shuffled, and finally a Hand class that holds those Cards that have been dealt to each player from the Deck.

