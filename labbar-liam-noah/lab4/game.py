import level as l

def find_player(level): # hittar specifikt spelaren på x&Y kordinaterna
    player = {'x':0,'y':0} # dict med x y kordinater
    players = l.entity_locations(level, 'player') 
    player['x'] = players[0][0]
    player['y'] = players[0][1]
    return player

def user_input(): # funktionen skickar ut kordinat justeringar
    print('(w)up, (d)right, (s)down, (a)left, (g)give up')
    while True:
        player_input = input('')
        if player_input == 'a':
            return {'x':-1,'y':0}
        if player_input == 's':
            return {'x':0,'y':1}
        if player_input == 'd':
            return {'x':1,'y':0}
        if player_input == 'w':
            return {'x':0,'y':-1} # Grid systemet går y neråt, därför är 'uppåt' y:-1
        if player_input == 'g':
            return "give up"


def player_can_move(level,player,move_direction): # 
    target_tile = l.check_level(level, move_direction['x']+player['x'], move_direction['y']+player['y']) # Vad finns på platsen vi vill gå till

    if target_tile == 'floor' or target_tile == 'storage': # Spelaren får alltid gå till dessa
        return True
    if target_tile == 'crate': # Spelaren får ibland gå till lådor
        crate_location = {'x': player['x']+move_direction['x'], 'y': player['y']+move_direction['y']} # Lådan finns på platsen vi vill flytta oss till så vi använder samma utränking
        return crate_can_move(level, crate_location, move_direction)
    return False # Endast väggar överblir, så vi behöver inte kolla med en if sats

def crate_can_move(level, crate_location, move_direction):
    target_tile = l.check_level(level, move_direction['x']+crate_location['x'], move_direction['y']+crate_location['y']) # Dit craten kommer puttas
    if target_tile == 'floor' or target_tile == 'storage': # De ända platserna som lådor får flyttas till
        return True
    return False

def move_player(level,player,move_direction):
    # Flytta lådan om den finns
    if(l.check_level(level, player['x']+move_direction['x'], player['y']+move_direction['y']) == 'crate'):
        l.set_entity(level, player['x']+move_direction['x']*2,player['y']+move_direction['y']*2, 'crate')
    # Flytta spelare
    l.set_entity(level,player['x']+move_direction['x'], player['y']+move_direction['y'],'player')
    # Rensa gammal spelare
    l.remove_entity(level, player['x'], player['y'])
    # Uppdatera spelarposition
    player['x'] += move_direction['x']
    player['y'] += move_direction['y']

def win_condition(level):
    for tile in level['board']:
        if level['board'][tile] == 'storage': 
            if l.check_level(level, tile[0], tile[1]) != 'crate':
                return False
    return True 
