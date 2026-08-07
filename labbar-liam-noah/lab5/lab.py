#! /usr/bin/env python3
# -*- coding:utf-8 -*-
from ast import Lambda
import pathlib # Path modifiering
import os # Path namn modifiering
from colorama import Fore, Style # text color styling 

def calculate(length, lambd):
    result = 1
    for n in range(2, length+1):
        result = lambd(n, result)
    return result

def dbsearch(db, field, search):
    result = []
    for entry in db:
        if search in entry.get(field):
            result.append(entry)
    return result 

def contains(element, list):
    for e in list:
        if element == e:
            return True
    return False

# kommando skal

def command():
    wd = pathlib.Path('.').resolve()

    while True: # oändlig loop.
        print(Fore.BLUE, end='')
        print('command> ', end='')
        print(Style.RESET_ALL, end='')
        answer = input()

        if answer == None:
            pass

        elif answer == 'pwd':
            print(wd)

        elif answer == 'ls':
            for subdir in wd.iterdir():
                print(os.path.basename(subdir))
        
        elif answer.split()[0] == 'cd' and 2 <= len(answer.split()):
            wd = (wd / answer.split()[1]).resolve()

        elif answer.split()[0] == 'cat' and 2 <= len(answer.split()):
            print(open(wd / answer.split()[1]).read())


# uppgift 5e
def generate_list(function, whole_number):
    result = []
    for n in range(1, whole_number+1): # magic number, matchar körexempel, börjar på 1
        result.append(function(n)) # lägg till svaret av funktionen
    return result 

def add(n,m): return n + m

# uppgift 5f partial
def partial(function, value):
    #returnera en ny funktion som den angivna funktionen med värdet bundet till det
    return lambda val1: function(value, val1) # lambda in variabel: funktion invariabel + value 

# uppgift 5g compose

def compose(F_a, F_b):
    #lambda syntax (enligt liam): funktion(parameter) = lambda parameter: expression 
    #F_res(x) = F_a(F_b(x)) 
    F_res = lambda value: F_a(F_b(value)) 
    return F_res

# uppgift 5h filter och mapped result

def make_filter_map(filter_func, map_func):
    # tar in filter och map funktionen som argument
    # funktionen ska returnera en funktion som tar en lista som argument. 
    # applicerar mapp funktionen på varje element i listan som filter funktionen är sann för. 
    # make_filter_map ska använda funktionerna partial och compose från tidigare uppgifter för 
    # att sätta ihop map och filter med indatafunktionerna.

    #map_loop = lambda l: map(map_func,l)
    
    func = compose(partial(map, map_func), partial(filter, filter_func))
    final_func = compose(list,func) # gör func svaret till en lista. och retunerar en funktion som har lista som argument
    return final_func

    # Loopa genom lista, om filter returnar false, tag bort. Loopa genom ny lista, kör värden genom map.


    #___________________________________________________________________________________________________________________________________________________________________-

def main5a():
    print(calculate(512, lambda x,y: x+y))
    print(calculate(512, lambda x,y: x*y))
    
def main5b():
    db = [
        {'name': 'Jakob', 'position': 'assistant'},
        {'name': 'Åke', 'position': 'assistant'},
        {'name': 'Ola', 'position': 'examiner'},
        {'name': 'Henrik', 'position': 'assistant'}
    ]

    print(dbsearch(db, 'position', 'examiner'))


    
def main5c():
    haystack = 'Can you find the needle in this haystack?'.split()

    print(contains('find', haystack))
    print(contains('needle', haystack))
    print(contains('haystack', haystack))
    
def main5d():
    command()
    
def main5e():
    mirror = lambda x: x
    print(generate_list(mirror, 4))
    stars = lambda n :'*' * n
    print(generate_list(stars, 5))
    
    
    
def main5f():
    add = lambda n, m: n+m
    add_five = partial(add, 5)
    print(add_five(3))
    print(add_five(16))

def main5g():
    multiply_five = lambda n: n*5
    add_ten = lambda x: x+10

    composition = compose(multiply_five, add_ten)
    print(composition(3))

    another_composition = compose(add_ten, multiply_five)
    print(another_composition(3))
    
def main5h():
    process = make_filter_map(lambda x: x % 2 == 1, lambda x: x * x)
    print(process(range(10)))

    

