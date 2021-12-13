values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def __str__(self):
        hand_comp = ''  # start with an empty string
        for card in self.cards:
            hand_comp += '\n ' + card.__str__()  # add each Card object's print string
        return f'The Hand has these cards: {hand_comp} \nWith total value = {self.value}'

    def add_card(self, card):
        print("Not yet implemented")

