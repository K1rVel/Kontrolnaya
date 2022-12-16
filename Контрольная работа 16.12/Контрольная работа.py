#Контрольная работа задача №18
class Alchemy:
    def __init__(self, element_1: str, element_2: str):
        self.element_1 = element_1
        self.element_2 = element_2

    def __add__(self):
        return self.element_1[:3] + self.element_2[:3]


alchemy = Alchemy('Aurum', 'Ferrum')
print(alchemy.__add__())