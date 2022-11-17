""" TODO write a program that will:
1. gets name from user and stores it in variable called player_name
the message that the user will see should be: Hello, whats your name?
2. gets the board size from the user and stores in variable called board_size, the value should be an **integer**
the message that the user will see should be: <name>, please choose board size:
3. gets the required number of mines and stores in variable called number_of_mines this is also should be an integer
the message that the user will see should be: <name>, for board size <board_size>, choose number of mines to allocate:
4. print summery of all data
"""
player_name = input("Hello, whats your name?")
board_size = int(input(f"{player_name}, please choose board size:"))
number_of_mines = int(input(f"{player_name}, for board size {board_size}, choose number of mines to allocate:"))
print(f"{player_name}, the board size is: {board_size}, number of mines is: {number_of_mines}. ENJOY!")