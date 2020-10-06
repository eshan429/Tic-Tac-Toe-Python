# Basic Tic-Tac-Toe game
# 
# Allows you to use custom tokens and player names and keeps track of scores over multiple rounds

# clear_output will not work outside of Jupyter Notebook, print a few newlines to clear current view
# from IPython.display import clear_output

#Set custom markers and default player names
global_markers = ['X', 'O']
name_keys = ['Player 1', 'Player 2']

# Global varaibles to keep track of names, markers & score over multiple games
names = {name_keys[0]:'', name_keys[1]:''}
markers = {name_keys[0]:'', name_keys[1]:''}
score = {name_keys[0]:0, name_keys[1]:0}

# Example board that diplays when you start your first game to help you understand the position numbers
# Also used as checking if input is valid ---------> Removed in refactor
example_board = [str(x) for x in range(0, 10)]

# Asks for Player Names in the first game only
def player_names(pl_num):
    s = input('Enter {} Name: '.format(name_keys[pl_num])).capitalize()
    return s if s != '' else name_keys[pl_num]


# Asks for marker for player 1 and assigns the other to player 2
def player_markers(all_markers):
    while True:
        mark = input('Choose a marker for {} ({} or {}): '.format(names[name_keys[0]], all_markers[0], all_markers[1])).upper()

        if mark not in all_markers:
            print("Please choose either '{}' or '{}'".format(all_markers[0], all_markers[1]))
            continue
        else:
            conf = input("You chose '{}' for {}. Press 'Y' to confirm or any other key to choose again: ".format(mark, names[name_keys[0]]))
            if conf.lower() == 'y':
                all_markers.remove(mark)
                return (mark, all_markers[0])
            else:
                continue


# The mighty board printer
def print_board(board):
#     clear_output()
    print('\n')*100
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('--|---|--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('\n')


# Check if move is valid (number is between 1-9 and cell is empty) and place token
def move(pl_num, board, pl_markers):
    while True:
        cell = input('{} choose a cell to play: '.format(names[name_keys[pl_num]]))
        if not cell.isdigit() or int(cell) not in range(1,10):
            print("Please enter a number between 1 and 9!")
            continue
        elif board[int(cell)] != ' ':
            print("Cell already occupied, please choose another cell!")
            continue
        else:
            board[int(cell)] = pl_markers[name_keys[pl_num]]
            print_board(board)
            break


# Super messy win check
def win_check(board, last_move_player, pl_markers):
    check_marker = [pl_markers[name_keys[last_move_player]]]*3

    return True if (board[1:4]==check_marker) or (board[4:7]==check_marker) or (board[7:]==check_marker) or                (board[1:8:3]==check_marker) or (board[2:9:3]==check_marker) or (board[3::3]==check_marker) or                (board[1::4]==check_marker) or (board[3:8:2]==check_marker) else False


# Setup player names, tokens & display example board - runs for first game only
def initializer(pl_names, pl_markers):
    all_markers = global_markers.copy()

    pl_names[name_keys[0]] = player_names(0)
    pl_names[name_keys[1]] = player_names(1)
    
    markers_tuple = player_markers(all_markers)
    pl_markers[name_keys[0]] = markers_tuple[0]
    pl_markers[name_keys[1]] = markers_tuple[1]

    print_board(example_board)
    print("Here's how the board is numbered. Enter a number when prompted to place your marker in that cell.")
    print("If the cell is already occupied, you'll be prompted to choose another cell.\n")


# Play Ball
# Would using a list be a better way to hold start_player & start_adjuster from a variable management perspective
def play_game(pl_names, pl_markers, pl_score, first = True, start_player = 0, start_adjuster = 1):
    if first:
        initializer(pl_names, pl_markers)
        pl_score[name_keys[0]] = 0
        pl_score[name_keys[1]] = 0
        
    game_board = [' ']*10
    game_board[0] = '#'

#     print(pl_names, pl_markers, sep='\n')

    curr_player = start_player
    adjuster = start_adjuster
    
    while True:
        move(curr_player, game_board, pl_markers)
        if win_check(game_board, curr_player, pl_markers):
            pl_score[name_keys[curr_player]] += 1
            print("{} WINS!".format(pl_names[name_keys[curr_player]]))
            break
        elif ' ' not in game_board:
            print("Game Tied")
            break
        else:
            curr_player += adjuster
            adjuster *= -1
    
    print("Current Score --- {}:{} - {}:{}".format(pl_names[name_keys[0]],pl_score[name_keys[0]],pl_names[name_keys[1]],pl_score[name_keys[1]]))
    
    play_on = input("Would you like to play another game? Press 'Y' to play again or any other key to exit: ")
    if play_on.lower() == 'y':
#         clear_output()
        print('\n')*100
#         The logic was if start_player == 0 with if and else blocks reversed by as start_player will only by 1 or 0,
#         I've simplified the logic
#         (If you can call having to write multiple lines of comments to explain the logic simplifying the code that is)
        if start_player:
            start_player = 0
            start_adjuster = 1
        else:
            start_player = 1
            start_adjuster = -1
        play_game(names, markers, score, False, start_player, start_adjuster)
    else:
#         clear_output()
        print('\n')*100
        print("Final Score --- {}:{} - {}:{}".format(pl_names[name_keys[0]],pl_score[name_keys[0]],pl_names[name_keys[1]],pl_score[name_keys[1]]))


# Unused Blocks after refactoring

# def print_example_board():
#     clear_output()
#     print("Here's how the board is numbered. Enter a number when prompted to place your marker in that cell.")
#     print("If the cell is already occupied, you'll be prompted to choose another cell.\n")
#     print(example_board[1] + ' | ' + example_board[2] + ' | ' + example_board[3])
#     print('--|---|--')
#     print(example_board[4] + ' | ' + example_board[5] + ' | ' + example_board[6])
#     print('--|---|--')
#     print(example_board[7] + ' | ' + example_board[8] + ' | ' + example_board[9])


play_game(names, markers, score)
