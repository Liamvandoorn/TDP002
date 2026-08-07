#! /usr/bin/env python3

# uppgift 6a

def linear_search(li, value, function):
    if value == function(li[0]):
        return li[0]
    else:
        return linear_search(li[1:],value, function) # upptäckte efteråt att return behövde vara här för att funktionen skulle anropas igen. 


# uppgift 6b binär sökning

def binary_search(haystack, needle, function):
    if needle == function(haystack[len(haystack)//2]): # binär sökning, börja u mitten.
        return haystack[len(haystack)//2]
    elif needle < function(haystack[len(haystack)//2]): # stora bokstäver kommer först, alfabetet går baklänges i storlek. om needle är mindre än hälften
        return binary_search(haystack[:len(haystack)//2], needle, function)
    else:
        return binary_search(haystack[len(haystack)//2:], needle, function) # om needle är större än hälften



def insertion_sort(db, function):

    #från vänster till höger kolla på andra elementet i listan med I,
    #kolla om det är större än en alla tidigare element.
    #sätt elementet framför elementet det är större än men bakom elementet det är mindre än,
    #inkrementera i

    for i in range(0, len(db)):
        key_in_list = function(db[i])
        for j in range(i, 0, -1): # loopa igenom alla element innan i.
            if key_in_list < function(db[j-1]): # om det elementet är större
                db[j], db[j-1] = db[j-1], db[j] # byt plats på elementen i listan db
            else:
                break; #yay det stämmer
    return db 


def quick_sort(db, function):
    db = db.copy()
    if len(db) <= 1:
        return db
    else:
        # pivot=längd av lista//2
        pivot =  function(db[0])
        # sortera mindre, vänster, sortera större, höger.
        smaller=[]
        bigger=[]
        # loopa igenom hela listan db
        for item in range(len(db)):
            if function(db[item]) > pivot:
                bigger.append(db[item])
            elif function(db[item]) < pivot:
                smaller.append(db[item])
        for item in bigger: #
            db.remove(item)
        for item in smaller:
            db.remove(item)

        return quick_sort(smaller, function) + db + quick_sort(bigger, function)





def upg6a():
    imdb = [
        {'title': 'The Rock', 'actress': 'Nicholas Cage', 'score': 11},          
        {'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10},    
        {'title': 'Black Hawk Down', 'actress': 'Eric Bana', 'score': 12}
    ]

    print(imdb)
    print(linear_search(imdb, 10, lambda e: e['score']))

def upg6b():
    people = [{'name': 'Pontus', 'age': 30},
              {'name': 'Sara', 'age': 20},
              {'name': 'Xavier', 'age': 19}]
    
    print(people)
    print(binary_search(people, 'Pontus', lambda e: e['name']))

def upg6c():      
    db1 = [
    ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
    ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
    ]
    
    print(db1)

    insertion_sort(db1, lambda e: e[0])

    print(db1)

def upg6d():
    db2 = [
    ('j', 'g'), ('a', 'u'), ('k', 'l'), ('o', 'i'),
    ('b', 's'), ('@', '.'), ('p', 's'), ('o', 'e')
    ]

    print(db2)
    print('')
    print(quick_sort(db2, lambda e: e[0]))

def main():
    ans = input(':')
    if ans == 'a':
        upg6a()
    elif ans == 'b':
        upg6b()
    elif ans == 'c':
        upg6c()
    elif ans == 'd':
        upg6d()
    else: 
        main()

main()
