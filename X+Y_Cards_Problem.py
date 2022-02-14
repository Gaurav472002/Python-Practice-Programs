

# Twenty random cards are placed in a row all face down. A turn consists of taking two adjacent cards where the left
# one is face up and the right one can be face up or face down and flipping them both. Show that this process must
# terminate. (with all the cards facing up).

# Let face down cards be '1' and face up cards be '0'
import random


def flipCards(cards):
    print("Initial:", cards)
    while '1' in cards:  # until there is a face down card in the stack
        random_index = random.randint(0, len(cards) - 1)  # changing the card's position randomly

        if cards[random_index] == '1':  # if a card is faced down
            cards[random_index] = '0'  # make card face up

        if random_index + 1 < len(cards):  # don't change the last card
            if cards[random_index + 1] == '1':  # If a card is faced down make it up
                cards[random_index + 1] = '0'
            else:  # If a card is faced up make it down
                cards[random_index + 1] = '1'
        print(cards)
    print("Thus the series terminated with all cards faced up")


if __name__ == '__main__':
    cards = list("1111")  # Strings are immutable
    flipCards(cards.copy())  # prevents changes in the deck of cards itself !































# another method
# def transform(b):
#     for i in range(len(b)-1):
#         if b[i] == '1':
#             b[i] == '0'
#             if b[i+1] == '0':
#                 b[i+1] = '1'
#             else:
#                 b[i+1] = '0'
#     return b


# if __name__ == "__main__":
#     a = list("011111000")
#     print(a)
#     while a != transform(a.copy()):
      
#             a = transform(a.copy())
#     print(a)
   
