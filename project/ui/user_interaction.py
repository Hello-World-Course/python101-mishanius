def is_name_valid(name):
    return len(name) > 2


def is_board_size_valid(board_size):
    return 0 < board_size < 26


def is_number_of_mines_valid(board_size, number_of_mines):
    return 0 < number_of_mines < 0.5 * board_size * board_size


def register_user():
    name = None
    board_size = None
    number_of_mines = None
    temp_name = input("Hello, whats your name?")
    if is_name_valid(temp_name):
        name = temp_name
        temp_board_size = int(input(f"{name}, please choose board size:"))
        if is_board_size_valid(temp_board_size):
            board_size = temp_board_size
            temp_number_of_mines = int(
                input(f"{name}, for board size {board_size}, choose number of mines to allocate:"))
            if is_number_of_mines_valid(board_size, temp_number_of_mines):
                number_of_mines = temp_number_of_mines
        else:
            print(f"{name}, you entered illegal board size")
    else:
        print("Your name is too short")
    return name, board_size, number_of_mines
