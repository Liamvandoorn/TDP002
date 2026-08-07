# ADT Kortlek
import card as c
import random

# Konstruktor
def create_deck(): 
    deck = []
    for suit in range(1,3):
        for rank in range(1,14):
            deck.append(c.create_card(rank, suit))        
    # Lägg til 2 jokrar
    deck.append(c.create_card("Joker A"))
    deck.append(c.create_card("Joker B"))    
    return deck

# Funktion för att flytta ett kort i kortleken till en annan plats
def move_card(deck, index, steps): 
    if (index + steps > len(deck)): 
        steps -= len(deck) 
    elif(index + steps < 0):
        steps += len(deck)  
    deck.insert(index + steps,deck.pop(index))
        

# Printar kortleken på ett läsbart sätt
def print_deck(deck):
    for card in deck:
        c.display_card(card)

# Få värdet av ett kort på ett index
def value_by_index(deck, index):
    return c.get_value(deck[index])

# Få index av kort
def find_card(deck, rank, suit=5):
    target_card = c.create_card(rank, suit) # skapar en kopia av kortet vi söker. Används för att lätt jämföra. 
    for card in deck:
        if (target_card == card): # checkar om kortet finns i decken, om det finns ett likadant kort retunerar vi indxet på det kortet.
            return deck.index(card)

# Blanda kortlek
def shuffle_deck(deck): # shuffle är en list funktion som blandar den.
    random.shuffle(deck)

# Dela kortlek
def split_deck(deck, index): 
    deck_split = []
    for card in range(index):
        deck_split.append(deck.pop(0))
    return deck_split
    
# Sätt ihop kortlek
def attatch_decks(deck_1, deck_2):
    for card in deck_2: # undviker en nestlad lista med for loop.
        deck_1.append(card)
    return deck_1

# Hur många kort har kortleken
def deck_size(deck): 
    return len(deck)
