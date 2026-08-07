#! /usr/bin/env python3
# -*- coding: utf-8 -*-

def create_shopping_list():
    return ['Kurslitteratur', 'Anteckningsblock','Penna']

def shopping_list(slist):
    for i in range(len(slist)): # för så lång som listan är, printa ut varje element i listan.
        print(i+1, slist[i]) # i+1 för att inte skriva ut kurslitteraturen som 1 och inte 0. slist[i] skriver ut varje element för vajre index i for loopen. 

def shopping_add():
    
    
#def shopping_edit():

#def shopping_remove():

