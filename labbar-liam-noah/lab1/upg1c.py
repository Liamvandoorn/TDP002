#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Funktion som kollar om talet är jämt delbart med talen 1-13
def check(n):
    divisible = True
    for i in range(1, 14):
        if(n%i != 0):
            divisible = False
    return divisible

smallest = 0 # Denna variabel kommer iterera genom alla tal tills det hittar det minsta talet delbart med 1-13
found = False # Används till while loopen

# Kollar tal tills ett tal delbart med 1-13 hittas
while found == False:
    smallest += 1
    found = check(smallest)

# Svaret
print(smallest)

