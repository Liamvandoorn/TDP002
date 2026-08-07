#!/usr/bin/env python3
#-*- coding: utf-8 -*-

namn = input("Vad heter du: ")
print("Hej {0}!".format(namn))
ålder = int(input("Mata in din ålder: "))
print("Du föddes år {1}-{0}".format(2022 - ålder, 2021 - ålder))
län = input("Vilket län föddes du i: ") 


#Strings är list by default i python. vi kan därför använd listor anrop [] för att hämta en viss range av strängens bokstäver.

#f funktionen tillåter dig att anropa tidigare skapade variabler inom {}.

# : väljer range/intervall, exempel [0:hälften av strängen] ger första halvan
# län[len(län)//2:] = variabel[bestämd längd//2:] (när [x:] lämnas tomt tar det i slutet av strängen)

""" i detta fall önskar vi även använda operatorer / + - * för att
justera strängens valda range. """

print(f"\nFörsta havan av ditt namn och andra halvan av ditt län är: {namn[0:len(namn)//2]}{län[len(län)//2:]}")
