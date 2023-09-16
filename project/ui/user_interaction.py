name = input("Hello, whats your name?")
board_size = None
number_of_mines = None

error = False
if len(name) <= 2:
    name = None
    error = True
    print("Your name is too short")
if not error:
    board_size = int(input("Michael, please choose board size:"))
    if not 0 < board_size < 26:
        board_size = None
        error = True
        print(f"{name} you entered illegal board size")
if not error:
    number_of_mines = int(input(f"{name}, for board size {board_size}, choose number of mines to allocate:"))
    if not 0 < number_of_mines < 10:
        number_of_mines = None
        error = True
        print(f"{name} you entered illegal number of mines")
if not error:
    print(f"{name} the board size is: {board_size}, number of mines is: {number_of_mines}. ENJOY!")
