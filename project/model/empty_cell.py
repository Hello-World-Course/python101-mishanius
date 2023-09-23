from project.model.cell import Cell


class EmptyCell(Cell):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.value = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def str_as_clicked(self):
        return " " if self.value is None or self.value == 0 else str(self.value)
