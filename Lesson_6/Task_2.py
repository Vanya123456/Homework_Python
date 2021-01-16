class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        return self._length * self._width * 25 * 5


a = Road(15, 5)
a.mass()
