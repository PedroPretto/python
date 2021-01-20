import random
#funcoes
def display_board(board):
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')
    print('--------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('--------------')
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')

#display_board([' ',' ',' ',' ',' ',' ',' ',' ',' ',' '])

def player_input():
    marker = ''

    while not (marker == 'X' or marker =='O'):
        marker = input('Player1: Voce quer ser X ou O?').upper()
    if marker == 'x':
        return ('X','O')
    return ('O','X')

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board, mark):
    return ((board[9] == mark and board[8] == mark and board[7] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark)
    )

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    return 'Player 1'

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for i in range(0,10):
        if space_check(board, i):
            return False
    return True
def player_choice(board):
    position = ' '
    
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Escolha sua jogada (1-9')
    return int(position)
def replay():

    return input('Quer jogar novamente? SIM ou NAO').lower().startswith('s')

#
#
#
#jogo

print('Bem vindo ao jogo da velha!')

while True:
    board = [' '] * 10
    player1_marker,player2_marker = player_input() #retorna uma tupla
    turn = choose_first()
    print(turn + ' comeca!')

    game_on = True

    while game_on:
        #jogador 1
        if turn == 'Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, player1_marker, position)
        #checa vitoria
        if win_check(board, player1_marker)
            display_board(board)
            print('Parabens, venceu!')
            game_on = False
        else:
            if full_board_check(board):
                display_board(board)
                print('Empate!')
                break

