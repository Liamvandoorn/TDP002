
# board ADT
graphics = {'player':'@','crate':'o','wall':'#','storage':'.','floor':' ','crate_on_storage':'*','player_on_storage':'+'}
inv_graphics = {v: k for k, v in graphics.items()}

def create_board():
    board = [["floor"]]
    return board  #returnerar boarden då temporära listornas värde läggs in här. 

def display_board(board):
    for y in range(len(board[0])):
        for x in range(len(board)):
            print(graphics[board[x][y]], end ='') # two dimensional array         
        print()  # ny linje för varje loop
   
def set_tile(board,x,y, tile): # magic number -1 för array börjar på 0, funktionen är även dynamisk och checkar om listan har utrymme för att lägga till itemet till din tile, om inte gör den en ny lista som låter dig göra det. 
    if x>len(board):
        for difference in range(x-len(board)):
            board.append(["floor"]*len(board[0]))
        
    if y>len(board[0]):
        diff = y-len(board[0])
        
        for index in range(len(board)):
            for difference in range(diff):
                board[index].append("floor")

    
    board[x-1][y-1] = tile

def check_tile(board,x,y):
    return board[x-1][y-1]


#def convert_text(text):
    

def load_level(board,level):
    # Rensar board
    for column in range(1,len(board)):
        board.pop(1)
    for row in range(1,len(board[0])):
       board[0].pop(1)
    set_tile(board, 1, 1, 'floor')

    # Laddar level
    with open('sokoban_levels.txt') as f:
        lines = f.readlines()
        for l in range(level-1):  # magic number -1 för att första banan redan är laddad, tänk 0.
            while True:
                popped_line = lines[0]
                lines.pop(0)
                if popped_line == '\n':
                    break
                     # poppa ur linjer tills vi hittar en linje som är \n
            # när vi hittar den linjen, breaka while true.
        for line in range(len(lines)):
            if lines[line] == "\n":
                break
            else:
                for letter in range(len(lines[line])):
                    if lines[line][letter] != "\n":
                        set_tile(board, letter+1, line+1, inv_graphics[lines[line][letter]])
                


        

    
#def create_board():
#    return {}

#def set_tile(board,x,y,tile):
#    board[(x,y)] = tile

#def display_board(board):
    #gör en lo
    
#def set_level():
    

    
    #####
    #   #
    #o  #
  ###  o##
  #  o o #
### # ## #   ######
#   # ## #####  ..#
# o  o          ..#
##### ### #@##  ..#
    #     #########
    #######
# X: 0 ->18 Y: 0 ->10
