class Cell:
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y
        self.clicked = False
        self.flag = False

    def set_clicked(self):
        self.clicked = True

    def is_clicked(self):
        return self.clicked

    def set_flag(self):
        self.flag = True

    def is_flaged(self):
        return self.flag

    def str_as_hidden(self):
        return "F" if not self.is_flaged() else "_"

    def str_as_clicked(self):
        raise NotImplementedError()

    def __str__(self) -> str:
        if self.is_clicked():
            return self.str_as_clicked()
        else:
            return self.str_as_hidden()


