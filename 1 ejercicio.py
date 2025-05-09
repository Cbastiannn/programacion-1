from abc import ABC, abstractmethod

class Estudiante(ABC):
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    @abstractmethod
    def mostrar_informacion(self):
        pass

class EstudianteUniversitario(Estudiante):
    def __init__(self, nombre, edad, grado, carrera):
        super().__init__(nombre, edad, grado)  # super() calls the parent class constructor
        self.carrera = carrera

    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nivel: Universitario, Carrera: {self.carrera}, Semestre: {self.grado}"

class EstudianteSecundaria(Estudiante):
    def mostrar_informacion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Nivel: Secundaria, Grado: {self.grado}"

# Creating instances of both classes
universitario = EstudianteUniversitario("Carlos Pérez", 20, "5°", "Ingeniería de Sistemas")
secundaria = EstudianteSecundaria("Ana Gómez", 16, "10°")

# Printing the information
print(universitario.mostrar_informacion())
print(secundaria.mostrar_informacion())
