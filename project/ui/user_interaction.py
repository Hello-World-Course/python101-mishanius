name = None
board_size = None
number_of_mines = None

name_temp = input("Hello, what's your name: ")
if len(name_temp) <= 2:
    print("Your name is too short")
else:
    # We are ok
    name = name_temp
    board_size_temp = int(input(f"{name}, please choose board size: "))
    if board_size_temp <= 0 or board_size_temp > 26:
        print(f"{name}, you have entered illegal board size")
    else:
        board_size = board_size_temp
        number_of_mines_temp = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate"))
        if number_of_mines_temp<= 0 or number_of_mines_temp > board_size*board_size//2:
            print(f"{name}, you have entered illegal number of mines")
        else:
            number_of_mines = number_of_mines_temp
            print(f"{name}, the bohard size is: {board_size}, number of mines is: {number_of_mines}. ENJOY!")