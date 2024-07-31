def is_name_valid(name):
    return len(name) > 2


def is_board_size_valid(board_size):
    try:
        board_size = int(board_size)
        return 0 < board_size < 26
    except ValueError:
        return False


def is_number_of_mines_valid(board_size, number_of_mines):
    try:
        board_size = int(board_size)
        number_of_mines = int(number_of_mines)
        max_mines = (board_size * board_size) // 2
        return 0 < number_of_mines <= max_mines
    except ValueError:
        return False


def register_user():
    # Name input
    name = input("Hello, whats your name? ")
    if not is_name_valid(name):
        print("Your name is too short")
        return None

    board_size = input(f"{name}, please choose board size: ")
    if not is_board_size_valid(board_size):
        print(f"{name}, you have entered illegal board size")
        return None

    board_size = int(board_size)

    number_of_mines = input(f"{name}, for board size {board_size}, choose number of mines to allocate: ")
    if not is_number_of_mines_valid(board_size, number_of_mines):
        print(f"{name}, you have entered illegal number of mines")
        return None

    number_of_mines = int(number_of_mines)

    return name, board_size, number_of_mines


user_name, user_board_size, user_num_mines = register_user()
print(f"name:{user_name}, board size:{user_board_size}, number of mines:{user_num_mines}")