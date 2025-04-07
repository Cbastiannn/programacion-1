class Estudiante:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__nota = 1

    def set_nota(self, nota):
        if 1 <= nota <= 5:
            self.__nota = nota
        else:
            print('Nota inválida, debe estar entre 1 y 100')

    def get_nota(self):
        return self.__nota

    def mostrar_datos(self):
        print(f"Estudiante: {self.__nombre}, Nota: {self.__nota}")



n=input('digite el nombre: ')
estudiante1 = Estudiante(n)
no = int(input('Digite la nota: '))
estudiante1.set_nota(no)

estudiante1.mostrar_datos()
