from abc import ABC, abstractmethod

class empleado(ABC):
    def __init__(self, salario,dias_de_trabajo):
        self.salario = salario
        self.dias_de_trabajo= dias_de_trabajo
       
    @abstractmethod
    def mostrar_informacion(self):
        pass

class dineroganado(empleado):
    def __init__(self, salario,dias_de_trabajo,extras):
        super().__init__(salario,dias_de_trabajo,) 
        self.extras = extras

    def mostrar_informacion(self):
        return f"salario: {self.salario},dias_de_trabajo: {self.dias_de_trabajo},extras: {self.extras}"


ganado= dineroganado("$300.000", "20","5")

print(ganado.mostrar_informacion())
