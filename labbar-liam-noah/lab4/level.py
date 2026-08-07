

graphics = {'player':'@','crate':'o','wall':'#','storage':'.','floor':' ','crate_on_storage':'*','player_on_storage':'+'} # För att rita grafik

# Källa: https://stackoverflow.com/questions/483666/reverse-invert-a-dictionary-mapping
inv_graphics = {v: k for k, v in graphics.items()} # För att läsa filer filens tecken. 

def create_board(): # Skapar en tom dict med tiles
    board = {}
    return board

def create_entities(): # Skapar en tom dict med entities
    entities = {}
    return entities

def create_level(): # Level består av brädan och entities (spelare och lådor)
    entities = create_entities()
    board = create_board()
    level = {'entities':entities, 'board':board}
    return level

def display(level): # funktion för att visa banan, tar in leveln du valt.
    height = 0 # Vi börjar vid 0 för att alltid justera höjd och bred till exakt det vi behöver på banan.
    for tile in level['board']: 
        if tile[1]+1 > height:
            height = tile[1]+1
    
    for row in range(height): # lopar antal rader som det ska finnas höjd
        width = 0 # sätter width till 0 som default
        board_tiles = [] # board_tiles skapar en lista för brädans entities
        entities = [] # skapar en lista för entiteterna i entities

        for tile in level['board']: 
            if tile[1] == row: 
               board_tiles.append(tile)  # lägger dessa tiles i en lista

               if tile[0]+1 > width: # om tilen ligger mer höger än bredden uppdateras den
                   width = tile[0]+1
                   
        for entity in level['entities']: # kollar om tiles i entities ligger på raden
            if entity[1] == row:
               entities.append(entity)  # lägger dessa tiles i en lista
               
        row_string =  ['floor']*width # Skapar en lista av mellanslag med längd som vi räknat ut. Kommer senare att konverteras till string
        for tile in board_tiles: # Fyller med alla föremål på denna rad från level['board']
            row_string[tile[0]] = level['board'][tile]
        
        for entity in entities: # Samma sak för entities, men om de finns på samma plats som storage ska det sparas
            if row_string[entity[0]] == 'storage':
                row_string[entity[0]] = level['entities'][entity] + '_on_storage'
            else:
                row_string[entity[0]] = level['entities'][entity]
        
        for index in range(len(row_string)): # Konverterar entries i listan till grafik. e.x. "player" -> "@"
            row_string[index] = graphics[row_string[index]]
        
        print("".join(row_string)) # Konverterar listan till en string och skriver ut (.join: Joina alla strängar i listan med stringen "" emmellan. Alltså sätts alla strings i listan ihop till en)

def set_tile(level, x, y, tile): # Ändrar brädan
    level['board'][(x,y)] = tile
#{k:v, (x,y):"", (1,2):"player"}, "player_on_storage"
def set_entity(level, x, y, enity): # Ändrar entities
    level['entities'][(x,y)] = enity

def remove_tile(level, x, y):
    del level['board'][(x,y)]

def remove_entity(level,x,y):
    del level['entities'][(x,y)]

def check_level(level,x,y): # Kollar vad för tile som finns vid en viss kordinat
    entity = level['entities'].get((x,y)) #level['entities'][(x,y)]
    if entity != None: # Prioritera eniteter
        return entity
    tile = level['board'].get((x,y)) # level['board'][(x,y)]
    if tile != None: # Kolla sedan efter brickor
        return tile
    return 'floor'

def check_tile(level, x, y):
    tile = level['board'].get((x,y))
    if tile != None:
        return tile
    return 'floor'

def entity_locations(level, target):
    list_of_locations = []
    for entity in level['entities']:
        if level['entities'][entity] == target:
            list_of_locations.append(entity)
    return list_of_locations

def tile_locations(level, target):
    list_of_locations = []
    for tile in level['board']:
        if level['board'][tile] == target:
            list_of_locations.append(tile)
    return list_of_locations

def load_level(level,level_number):

    # Laddar level
    with open('sokoban_levels.txt') as f:
        lines = f.readlines()
        for l in range(level_number-1):  # magic number -1 för att första banan redan är laddad, tänk 0.
            while True:
                popped_line = lines[0]
                lines.pop(0)
                if popped_line == '\n':
                    break
        for line in range(len(lines)):
            if lines[line] == "\n":
                break
            else:
                for letter in range(len(lines[line])-1): # magic number: sista bokstaven i varje rad är \n och vi har därför -1 för att inte itterera över den.
                    item = inv_graphics[lines[line][letter]] # inv graphics för att associera vårat item # till wall
                    if item == 'player'or item=='crate':
                        set_entity(level, letter,line, item)
                    if item == 'wall' or item == 'storage':
                        set_tile(level, letter, line, item)
                    if item[-11:] == '_on_storage':
                        set_tile(level, letter, line, 'storage')
                        set_entity(level, letter, line, item[:-11])
                   
                    

            
