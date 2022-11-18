""" TODO write a program that will:
1. gets name from user and stores it in variable called player_name
the message that the user will see should be: Hello, whats your name?
2. gets the board size from the user and stores in variable called board_size, the value should be an **integer**
the message that the user will see should be: <name>, please choose board size:
3. gets the required number of mines and stores in variable called number_of_mines this is also should be an integer
the message that the user will see should be: <name>, for board size <board_size>, choose number of mines to allocate:
4. print summery of all data
"""
player_name, board_size, number_of_mines = None, None, None
temp_player_name = input("Hello, whats your name?")
if len(temp_player_name) > 1:
    player_name = temp_player_name
    temp_board_size = int(input(f"{player_name}, please choose board size:"))
    if temp_board_size > 0 and temp_board_size < 26:
        board_size = temp_board_size
        temp_number_of_mines = int(
            input(f"{player_name}, for board size {board_size}, choose number of mines to allocate:"))
        if 0 < temp_number_of_mines <= 0.5 * board_size * board_size:
            number_of_mines = temp_number_of_mines
        else:
            print(f"{player_name}, you entered illegal number of mines")
    else:
        print(f"{player_name}, you entered illegal board size")
else:
    print(f"Your name is too short")
