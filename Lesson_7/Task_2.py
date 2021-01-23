from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def costume(self):
        pass


class My_Clothes(Clothes):
    def __init__(self, size, growth):
        self.size = size
        self.growth = growth

    @property
    def coat(self):
        return f'Расход ткани для изготовления пальто: {round(self.size / 6.5 + 0.5, 2)} метра.'

    @property
    def costume(self):
        return f'Расход ткани для изготовления костюма: {round(2 * self.growth + 0.3, 2)} метра.'

    @property
    def common_consumption(self):
        return f'Общий расход ткани для всех изделий: ' \
               f'{round(self.size / 6.5 + 0.5, 2) + round(2 * self.growth + 0.3, 2)} метра.'


c1 = My_Clothes(42, 171)
print(c1.coat)
print(c1.costume)
print(c1.common_consumption)
