#####################################################################
# author: Blaine Hord
# date: 2/2/2024
# description: Card game using object oriented programming and random module
#####################################################################

# import the shuffle and seed functions from the random library.
import random
from typing_extensions import clear_overloads

# set the seed
random.seed(9876543210)

# define the possible suits that the cards can have using a list.
POSSIBLESUITS = ["clubs", "diamonds", "hearts", "spades"]

# define lists of possible user inputs.
yeslist = ["", "yes", "y", "t", "true", "ye"]
nolist = ["no", "n", "nope", "nah"]

# class to define card parameters and methods.
class Card:

  # initialize the card with a suit and a value.
  def __init__(self, number, suit):
    self.number = number
    self.suit = suit

  # define an accessor for the number instance variable
  @property
  def number(self):
    return self._number

  # define an mutator for the number instance variable
  @number.setter
  def number(self, number):
    if isinstance(number, int):
      if number >= 2 and number <= 10:
        self._number = number
      else:
        self._number = 2
    else:
      raise ValueError("Number must be an integer between 2 and 10")

  # define an accessor for the suit instance variable
  @property
  def suit(self):
    return self._suit

  # define an mutator for the suit instance variable
  @suit.setter
  def suit(self, suit):
    if suit.lower() not in POSSIBLESUITS:
      self._suit = "clubs"
    else:
      self._suit = suit.lower()

  # overload the string operator to return a string representation of the card.
  def __str__(self):
    return f"{self.number} of {self.suit}"

  # overload the greater than operator to compare if the given card is greater than the other.
  def __gt__(self, other):
    return self._number > other._number

  # overload the less than operator to compare if the given card is less than the other.
  def __lt__(self, other):
    return self._number < other._number

  # overload the equal to operator to compare if two cards are equal.
  def __eq__(self, other):
    return self._number == other._number


# class to define the deck of cards.
class Deck:
  # initialize the deck with a list of cards
  def __init__(self):
    self.cards = []
    for number in range(2,11):
      for suit in POSSIBLESUITS:
        self.cards.append(Card(number, suit))

  # acessor for the cards instance variable
  @property
  def cards(self):
    return self._cards

  # mutator for the cards instance variable
  @cards.setter
  def cards(self, value):
    self._cards = value

  # shuffle function to shuffle the cards in the deck
  def shuffle(self):
    return random.shuffle(self._cards)

  # size function to return the size of the deck
  def size(self):
    return len(self._cards)

  # draw dunction to return the top card in the deck then remove it from the deck
  def draw(self):
    if self.size() > 0:
      card1 = self._cards[0]
      self._cards.pop(0)
      return card1
    else:
      return None

  # overload the string function to display the deck in a comma seperated list
  def __str__(self):
    if len(self._cards) == 0:
      return "[--empty--]"

    else:
      return "["+", ".join([str(card) for card in self._cards])+"]"

# class to deifne game parameters and methods
class Game:

  # initialize the game with a deck of cards and shuffle the deck twice
  def __init__(self):
    self.deck = Deck()
    self._deck.shuffle()
    self._deck.shuffle()

  # accessor for the deck instance variable
  @property
  def deck(self):
    return self._deck

  # mutator for the deck instance variable
  @deck.setter
  def deck(self, value):
    self._deck = value

  # function to start the game
  def start(self):
    print("-" * 40)
    print("Welcome to a basic game.")
    print("You and this program will take turns picking cards.")
    print("The one with the highest value card wins")
    print("-" * 40)
    ready = input("Are you ready to start? ")
    if ready.lower() in yeslist:
      self.play()

    if ready.lower() in nolist or self.deck.size() == 0:
      self.end()
      
    else:
      print("Invalid input. Please try again.")
      self.start()

  # function to end the game
  def end(self):
    print("Sorry to see you go")
    print("-----Remaining cards-----")
    print(self._deck)

  # function to play the game
  def play(self):
    while self.deck.size() >= 2:
      pCard = self._deck.draw() # draw a card for the player
      cCard = self._deck.draw() # draw a card for the computer
      self._deck.shuffle() # shuffle the deck
      print(f"You picked {pCard}, and I picked {cCard}")
      if pCard > cCard:
        print("YOU WIN")

      elif pCard < cCard:
        print("I WIN")

      else:
        print("TIE")

      again = input("Would you like to play again? ")
      if again.lower() in yeslist:
        continue

      elif again.lower() in nolist:
        self.end()
        break

      else:
        break

    else:
      print("Not enough cards to play")


Game().start()