#!/usr/bin/env python3
#-*- coding: utf-8 -*-

# skapar en funktion som checkar om något är ett primtal.

def checkPrime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# result variabeln använder vi i loopen för att lagra summan. 
result = 0

# itererar igenom alla värden 2 till 1000 (vi börjar på 2 eftersom vår funktion tror att 1 är ett primtal vilket det inte är) och adderar dem om de är primtal
for i in range(2, 1001):
    if checkPrime(i):
        result += i

# resultat
print(result)
