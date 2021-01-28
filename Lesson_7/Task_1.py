class Matrix:
    def __init__(self, user_input):
        self.input = user_input

    def __str__(self):
        return '\n'.join([' '.join([str(el) for el in line]) for line in self.input])

    def __add__(self, other):
        my_matrix = ''
        if len(self.input) == len(other.input):
            for line_1, line_2 in zip(self.input, other.input):
                if len(line_1) != len(line_2):
                    return 'Разный вид митриц!'

                user_sum = [x + y for x, y in zip(line_1, line_2)]
                my_matrix += ' '.join([str(el) for el in user_sum]) + '\n'
        else:
            return 'Разная вид матриц!'
        return my_matrix


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[2, 3], [4, 5], [6, 7], [1, 20]])
print(matrix_1)
print(matrix_2 + matrix_1)
