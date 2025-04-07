from abc import ABC, abstractmethod

class Estudiante(ABC):
    def __init__(self, nmate, nespañol):
        self.nmate = nmate
        self.nespañol = nespañol

    @abstractmethod
    def calcular_nota(self):
        pass

class Estudiante1(Estudiante):
    def calcular_nota(self):
        notafinal = (self.nmate + self.nespañol) / 2
        return notafinal

mate = float(input('Su nota de mate fue: '))
print(mate)
espa = float(input('Su nota de español fue: '))
print(espa)

estudiante1 = Estudiante1(nmate=mate, nespañol=espa)
nota_final = estudiante1.calcular_nota()
print("La nota final fue:", nota_final)


