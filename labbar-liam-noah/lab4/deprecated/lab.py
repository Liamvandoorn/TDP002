
# main
import board as b
import game_logic as gl

def main():

    board = b.create_board()
    b.load_level(board, int(input('choose level:  ')))
    print('')
    player = gl.find_player(board)

    win = False
    while (win == False):
        b.display_board(board)
        player_input = gl.move_input()
        if player_input == "give up":
            break
        print(gl.player_can_move(board,player,player_input))
        if gl.player_can_move(board,player,player_input):
            gl.move_player(board,player,player_input)

        win = gl.win_condition(board)
    if win == True:
        b.display_board(board)
        print('YOU WIN!')
    else:
        print('YOU ARE A "LOSER"!')
main()
