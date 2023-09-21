def parse_cmd(command):
    cmd, *params = command.split(" ")
    return cmd, params


def draw_board(board, k):
    number_of_spaces = len(str(len(board)))
    columns_names = " " * number_of_spaces + " " * 2 + " ".join([chr(ord('A') + i) for i in range(len(board))]) + "\n"
    board_draw = ""
    raise NotImplementedError("asdasd")
    for idx, row in enumerate(board):
        board_draw += f"{idx} |{'|'.join(map(lambda a: str(a), row))}|\n"
    return columns_names + board_draw
