class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        if self.nucleus - other.nucleus > 0:
            return Cell(self.nucleus - other.nucleus)
        else:
            print('К сожалению, обьединение этих клеток невозможно!')

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __floordiv__(self, other):
        if other.nucleus != 0:
            return Cell(self.nucleus // other.nucleus)
        else:
            print('На 0 делить нельзя!')

    def __str__(self):
        return f'Новая клетка с {self.nucleus} ячейками.'

    def make_order(self):
        star = ''
        count = 0
        while self.nucleus != 0:
            self.nucleus -= 1
            star += '*'
            count += 1
            if count % 5 == 0:
                star += '\n'
        print(star)


cell_1 = Cell(13)
cell_2 = Cell(2)
print(cell_1 // cell_2)
cell_1.make_order()
