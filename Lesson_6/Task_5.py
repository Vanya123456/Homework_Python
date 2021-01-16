class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')


class Pen(Stationery):
    def draw(self):
        print('Start writing')


class Pencil(Stationery):
    def draw(self):
        print('Start sketching')


class Handle(Stationery):
    def draw(self):
        print('Start painting')


pen = Pen('ручка')
pen.draw()
pencil = Pencil('карандаш')
pencil.draw()
handle = Handle('маркер')
handle.draw()
