def is_board_size_valid(number):
    return number > 0 and number < 26


def is_name_valid(name):
    return len(name) > 2


def is_number_of_mines_valid(number_of_mines, board_size):
    return number_of_mines > 0 and number_of_mines < 0.5 * board_size * board_size


def register_user():
    player_name, board_size, number_of_mines = None, None, None
    temp_player_name = input("Hello, whats your name?")
    if is_name_valid(temp_player_name):
        player_name = temp_player_name
        temp_board_size = int(input(f"{player_name}, please choose board size:"))
        if is_board_size_valid(temp_board_size):
            board_size = temp_board_size
            temp_number_of_mines = int(
                input(f"{player_name}, for board size {board_size}, choose number of mines to allocate:"))
            if is_number_of_mines_valid(temp_number_of_mines, board_size):
                number_of_mines = temp_number_of_mines
            else:
                print(f"{player_name}, you entered illegal number of mines")
        else:
            print(f"{player_name}, you entered illegal board size")
    else:
        print(f"Your name is too short")
    return player_name, board_size, number_of_mines
