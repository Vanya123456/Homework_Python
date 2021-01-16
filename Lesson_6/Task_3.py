class Worker:
    """Не совсем понятно из условия, нужно было в 4-ом параметре создать уже готовый словарь с зарплатой и премией
    для каждого сотрудника или же нужно давать возможность пользователю вводить их самостоятельно. Сделал по своему
    как понял."""
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        total = 0
        for val in self._income.values():
            total += int(val)
        print(total)


human = Position('Ivan', 'Buyukli', 'Welder', 5000, 400)
human.get_full_name()
human.get_total_income()

human_2 = Position('Frank', 'Anderwood', 'Kongresman', 20000, 5000)
human_2.get_full_name()
human_2.get_total_income()
