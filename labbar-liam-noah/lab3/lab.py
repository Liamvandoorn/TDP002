# Huvudprogram
import deck as d
#filtrering av text. 
import re 

def solitaire_keystream(length, deck):    
    key = ""
    
 
    while (len(key) < length):

        # Flyttar jokrar
        d.move_card(deck, d.find_card(deck, "Joker A"), 1)
        d.move_card(deck, d.find_card(deck, "Joker B"), 2)

        # Hittar första jokern och delar kortleken
        first_joker = min(d.find_card(deck, "Joker A"), d.find_card(deck, "Joker B"))
        deck_A = d.split_deck(deck, first_joker)

        # Hittar andra jokern och delar kortleken, magic number: +1 för att dela precis efter joker, så att båda jokrarna hamnar i del B
        last_joker = max(d.find_card(deck, "Joker A"), d.find_card(deck, "Joker B"))
        deck_B = d.split_deck(deck, last_joker+1) 

        # Överblivande kortlek blir del C
        deck_C = deck

        # Sätter ihop delarna baklänges
        deck = d.attatch_decks(deck_C, deck_B)
        deck = d.attatch_decks(deck, deck_A)

        # Steg 5 i algoritmen, magiska nummer -1 är för att få sista kortet från decksize, magiska nummer +1 är för att vi flyttar det sista kortet till början och sedan delar upp leken och flyttar till slutet, så vi vill flytta "värdet av sista kortet" kort och det sista kortet. 
        value_last_card = d.value_by_index(deck, d.deck_size(deck)-1)
        d.move_card(deck, d.deck_size(deck)-1, value_last_card+1)
        deck_split = d.split_deck(deck, value_last_card+1)
        deck = d.attatch_decks(deck, deck_split)
        
        # Skapar en bokstav utifrån kort använder chr casing av en int.
        unchecked_key = chr(64+d.value_by_index(deck, d.value_by_index(deck, 0))) # Använd en ASCII tabell som referens. Stora bokstäver har värden 64 - 90

        # Om kortet var en joker blir bokstaven en hakparantes, då förkastar vi resultatet och börjar om
        if str(unchecked_key) != "[":
            key += unchecked_key


    # När key strängen blir like lång som vi angivit length, retunera nyckeln. 
    return key

solitaire_deck = d.create_deck()    
d.shuffle_deck(solitaire_deck)

solitaire_deck_copy = solitaire_deck.copy()

#uppgift 3b kryptera text -------------------------------------------------------------

#konverterar siffror till bokstäver eller bokstäver till siffror (A=1, B=2,... Z=26)
#magic number: +64 för att se till så 1 = 65 = (A i ASCII)
def number_letter_conversion(x):
    if type(x) == int:
        result = str(chr(x + 64))
        return result
    else:
        result = (ord(x) - 64) #ord tar string till asciii värdet som int
        return result

def check_if_letter(letter):
    if number_letter_conversion(letter) < 0 or number_letter_conversion(letter) > 26:
        return False
    else:
        return True
    
def solitaire_encrypt(string_unchecked, deck):
    #slopa alla tecken förutom A - Z och konverta allt til versaler, sub gör resultatet till strängen
    string_unchecked = string_unchecked.upper()
    string = ""
    for element in string_unchecked:
        if check_if_letter(element):
            string += element
            

    #generera en nyckelfras med samma längd  av medelandet
    encryption_key = solitaire_keystream(len(string), deck)
    #konvertera strängen till tal.
    string_as_number = []
    for letter in string:
        string_as_number.append(number_letter_conversion(letter))

    encryption_key_as_number = []
    for letter in encryption_key:
        encryption_key_as_number.append(number_letter_conversion(letter))
    # Addera talen från medddelandet med talen i nyckelfrasen encryptionkeyasnumber + stringasnumber. if sum > 26 stega fram från början.
    encrypted_message = []
    for index in range(len(string_as_number)):
        encrypted_message.append((encryption_key_as_number[index] + string_as_number[index]))

    for index in range(len(encrypted_message)):
        if encrypted_message[index] > 26:
            encrypted_message[index] -= 26

    #konvertera talen till bokstäver via en for loop och sparar den i en string.
    encrypted_message_string = ""
    for element in encrypted_message:
        encrypted_message_string += number_letter_conversion(element)

    return encrypted_message_string


noahs_secret = solitaire_encrypt("Python", solitaire_deck)
print(noahs_secret)

#uppgift 3c dekryptera text ----------------------------------------------------------

def solitaire_decrypt(encrypted_string, deck):
    
    encryption_key = solitaire_keystream(len(encrypted_string), deck)
    #konvertera strängen till tal.
    enc_string_as_number = []
    for letter in encrypted_string:
        enc_string_as_number.append(number_letter_conversion(letter))

    encryption_key_as_number = []
    for letter in encryption_key:
        encryption_key_as_number.append(number_letter_conversion(letter))
    # Addera talen från medddelandet med talen i nyckelfrasen encryptionkeyasnumber + stringasnumber. if sum > 26 stega fram från början.
    decrypted_message = []
    for index in range(len(enc_string_as_number)):
        decrypted_message.append((enc_string_as_number[index] - encryption_key_as_number[index]))

    for index in range(len(decrypted_message)):
        if decrypted_message[index] < 0:
            decrypted_message[index] += 26

    #konvertera talen till bokstäver via en for loop och sparar den i en string.
    decrypted_message_string = ""
    for element in decrypted_message:
        decrypted_message_string += number_letter_conversion(element)

    return decrypted_message_string
    
print(solitaire_decrypt(noahs_secret, solitaire_deck_copy)) 
