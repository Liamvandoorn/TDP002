# ADT Kort

suits = {1:'Spades', 2:'Hearts',  3:'Diamonds', 4:'Clubs', 5:'Joker'} # ignorera 3,4, vi trodde det skulle vara 4 suits från början

# Konstruktor # icke specifierad suit blir 5 så att man kan skriva endast 1 argument när man vill ha en joker. ex. create_card("Joker A")
def create_card(rank, suit=5):
    if (type(rank) != str):
        card = [rank,suit]
    elif (rank == "Joker A"):
        card = ["A", suit]
    else:
        card = ["B", suit]
    return card

def get_suite(card):
    return card[1]

def get_value(card):
    value = 0
    if (card[1] == 5):
        value = 27
    else:
        value = (card[1]-1)*13 #-1 för att göra värdet till +13, rent mattematiskt 
        value += card[0] #
    return value
    
def display_card(card): 
    if (card[1] != 5): 
        print(card[0], "of", suits[card[1]])
    else:
        print(suits[card[1]], card[0]) # printa omvänt för joker.
