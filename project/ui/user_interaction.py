name = None
board_size = None
number_of_mines = None

input_name = input("Hello, what's your name: ")

if len(input_name) <= 2:
    print("Your name is too short")
else:
    name = input_name
    board_size_input = input(f"{name}, please choose board size: ")

    if not board_size_input.isdigit() or not (0 < int(board_size_input) < 26):
        print(f"{name}, you have entered illegal board size")
    else:
        board_size = int(board_size_input)
        max_mines = (board_size * board_size) // 2

        number_of_mines_input = input(f"{name}, for board size {board_size}, choose number of mines to allocate: ")

        if not number_of_mines_input.isdigit() or not (0 < int(number_of_mines_input) <= max_mines):
            print(f"{name}, you have entered illegal number of mines")
        else:
            number_of_mines = int(number_of_mines_input)
            print(f"{name}, the board size is: {board_size}, number of mines is: {number_of_mines}. ENJOY!")