# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
action = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
# define hand class
class Hand:
    def __init__(self):
        self.hand = []
    def __str__(self):
        return_string = "Hand contains"
        for card in self.hand:
            return_string = " " + str(card)
        return return_string
        #hand_list_join = ""
        #for i in range(len(self.hand)):
        #    hand_list_join += str(self.hand[i].suit + self.hand[i].rank + " ")
        #return "Hand contains " + hand_list_join	# return a string representation of a hand

    def add_card(self, card):
        self.hand.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        hand_values = 0
        for card in self.hand:
            hand_values += VALUES[card.get_rank()]
        #for hand in self.hand:
        if hand.get_rank() == "A" and (hand_values + 10) <=21: # if there is two aces, only can add 10 once, otherwise greater than 21
            return (hand_values + 10)
        else:
            return hand_values
        #hand_values = []
        #for i in range(len(self.hand)):
        #    hand_values.append(VALUES.get(self.hand[i].rank))
            
        #for j in range(len(self.hand)):
        #    if len(self.hand) == 0:
        #        return 0
        #    elif self.hand[j].rank != "A":
        #        return sum(hand_values)
        #    else:
        #        if sum(hand_values) + 10 <=21:
        #            return sum(hand_values) + 10
        #        else:
        #            return sum(hand_values) # compute the value of the hand, see Blackjack video'''
   
    def draw(self, canvas, pos):
        for card in self.hand:
            card.draw(canvas, pos)
            pos[0] += CARD_SIZE[0] + 20 #define the position for next card in hand
        #for i in range(len(self.hand)):
        #    self.hand[i].draw(canvas, [pos[0]+100*i,pos[1]])
                    
# define deck class 
class Deck:
    def __init__(self):
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit,rank))
        #for i in range(len(SUITS)):
        #    for j in range(len(RANKS)): 
        #                   self.deck.append(Card(SUITS[i],RANKS[j]))# create a Deck object

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)    # use random.shuffle()

    def deal_card(self):
        last = self.deck.pop(-1)
        self.deck.pop(-1)
        return last
            
    def __str__(self):
        return_string = "Deck contains"
        for card in self.deck:
            return_string += " " + str(card)
        return return_string
        #deck_list_join = ""
        #for i in range(len(self.deck)):
        #    deck_list_join += str(self.deck[i].suit + self.deck[i].rank + " ")
        #return "Deck contains " + deck_list_join	# return a string representing the deck  

#define event handlers for buttons
def deal():
    global my_deck, outcome, action, in_play, dealer_hand, player_hand, score
    my_deck = Deck()
    my_deck.shuffle()
    outcome = "Hit or stand?"
    if in_play == False:
        dealer_hand = Hand()
        player_hand = Hand()
        dealer_hand.add_card(my_deck.deal_card())
        player_hand.add_card(my_deck.deal_card())
        dealer_hand.add_card(my_deck.deal_card())
        player_hand.add_card(my_deck.deal_card())
        in_play = True
        action = ""
    else:
        score -= 1
        action = "You surrended"
        outcome = "New deal?"
        in_play = False

def hit():
    global my_deck, dealer_hand, player_hand, in_play, outcome, action, score
    if in_play == True:
        if player_hand.get_value() <= 21:
            player_hand.add_card(my_deck.deal_card())
            if player_hand.get_value() > 21:
                action = 'You busted and lost'
                outcome = "New deal?"
                score -= 1
                in_play = False
       
def stand():
    global in_play, dealer_hand, outcome, action, my_deck, score
    if in_play == False:
        action = "Not valid stand"
    else:
        while (dealer_hand.get_value() < 17):
            dealer_hand.add_card(my_deck.deal_card())
        if dealer_hand.get_value() > 21:
            action = "You win"
            score += 1
        elif dealer_hand.get_value() >= player_hand.get_value():
            action = "You lose"
            score -= 1
        else:
            action = "You win"
            score += 1
        in_play = False
        outcome = "New deal?"

# draw handler    
def draw(canvas):
    global outcome, action, player_hand, dealer_hand, CARD_BACK_SIZE, CARD_BACK_CENTER
    player_position = [100, 400]
    dealer_position = [100, 200]
    canvas.draw_text('Blackjack', (100, 100), 40, 'Red')
    canvas.draw_text('Dealer', (100, 150), 30, 'Black')
    canvas.draw_text('Player', (100, 350), 30, 'Black')
    canvas.draw_text(str(action), [350, 150], 30, 'Black')
    canvas.draw_text(str(outcome), [350, 350], 30, 'Black')
    canvas.draw_text("Score " + str(score), [400,100], 30, 'Black')
    player_hand.draw(canvas, player_position)
    dealer_hand.draw(canvas, dealer_position)
    if in_play == True:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100 + CARD_BACK_CENTER[0], 200 + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
   
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()
