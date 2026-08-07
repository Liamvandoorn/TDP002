
import board as b

#player movement
#player position
def find_player(board):
    # check current player position in index with for loop looping through the board (all the indexes)
    player = {'x':0, 'y':0}
    for column in board:
        player['x'] += 1
        player['y'] = 0 
        for row in column:
            player['y'] += 1 
            if row == 'player':
                return player # return player position as dictionary (x:found value,y:found value)
            
def move_input():
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
    


def player_can_move(board,player,move_direction):
    #check tile of move input
    target_tile = b.check_tile(board, move_direction['x']+player['x'], move_direction['y']+player['y'])
    if target_tile == 'floor' or target_tile == 'storage':
        return True
    if target_tile == 'crate' or target_tile == 'crate_on_storage':
        crate_location = {'x': player['x']+move_direction['x'], 'y': player['y']+move_direction['y']}
        return crate_can_move(board, crate_location, move_direction)
    return False
        
    #if yes
def crate_can_move(board, crate_location, move_direction):
    target_tile = b.check_tile(board, move_direction['x']+crate_location['x'], move_direction['y']+crate_location['y'])
    if target_tile == 'floor' or target_tile == 'storage':
        return True
    return False



def move_player(board,player,move_direction):
    # vi får input
    # checka vart vi står
    current_tile = b.check_tile(board, player['x'], player['y'])
    # vart vill vi gå
    target_tile = b.check_tile(board, move_direction['x']+player['x'], move_direction['y']+player['y'])

    # draw new player
    if target_tile == 'floor' or target_tile == 'crate':
        b.set_tile(board, move_direction['x']+player['x'], move_direction['y']+player['y'], 'player')
    else:
        b.set_tile(board, move_direction['x']+player['x'], move_direction['y']+player['y'], 'player_on_storage')
    # clear old player position
    if current_tile == 'player':
        b.set_tile(board, player['x'], player['y'], 'floor')
    else:
        b.set_tile(board, player['x'], player['y'], 'storage')


    # move crate
    if target_tile == 'crate' or target_tile == 'crate_on_storage':
        crate_location = {'x': player['x']+move_direction['x'], 'y': player['y']+move_direction['y']}
        move_crate(board, crate_location, move_direction)

    # move player
    player['x'] += move_direction['x']
    player['y'] += move_direction['y']

def move_crate(board, crate_location, move_direction):
    target_tile = b.check_tile(board, move_direction['x']+crate_location['x'], move_direction['y']+crate_location['y'])
    if target_tile == 'floor':
        b.set_tile(board, crate_location['x']+move_direction['x'],crate_location['y']+move_direction['y'], 'crate')
    else:
        b.set_tile(board, crate_location['x']+move_direction['x'],crate_location['y']+move_direction['y'], 'crate_on_storage')


        
def win_condition(board):
    for column in board: 
        for row in column: 
            if row == 'crate':
                return False
    return True
            
