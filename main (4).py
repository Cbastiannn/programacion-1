from abc import ABC, abstractmethod

class Menu(ABC):
    def __init__(self):
        self.opciones = {} 
        
    @abstractmethod
    def mostrar_opciones(self):
        pass
    
    @abstractmethod
    def ejecutar_opcion(self, opcion):
        pass

class MenuConcreto(Menu):
    def __init__(self):
        super().__init__()
        self.opciones = {
            "1": ("sumar numeros", self.sumar_numeros),
            "2": ("restar numeros", self.restar_numeros),
            "3": ("multiplicar numeros", self.multiplicar_numeros),
            "4": ("salir", self.salir)
         }
        self.ejecutando = True
        
    def mostrar_opciones(self):
        print("\n--- Menú ---")
        for clave, (descripcion, _) in self.opciones.items():
            print(f"{clave}. {descripcion}")
    def ejecutar_opcion(self, opcion):
        if opcion in self.opciones:
            self.opciones[opcion][1]()  
        else:
            print("ingrese un numero valido")
    
    def sumar_numeros(self):
         try:
            a = int(input("Ingrese el primer número: "))
            print(a)
            b = int(input("Ingrese el segundo número: "))
            print(b)
            r=a+b
            print( 'Resultado de la suma:',a,'+',b,'=',r)
         except ValueError:
            print(" Error: Debes ingresar números válidos.")
    def restar_numeros(self):
        try:
            a = int(input("Ingrese el primer número: "))
            print(a)
            b = int(input("Ingrese el segundo número: "))
            print(b)
            r=a-b
            print(' Resultado de la resta :',a, '-',b,'=',r,)
        except ValueError:
            print(" Error: Debes ingresar números válidos.")
    def multiplicar_numeros(self):
        try:
            a = int(input("Ingrese el primer número: "))
            print(a)
            b = int(input("Ingrese el segundo número: "))
            print(b)
            r=a*b
            print(' Resultado de la multiplicacion',a, '*',b,'=',r)
        except ValueError:
            print(" Error: Debes ingresar números válidos.")

    def salir(self):
        print(" Saliendo del menú...")
        self.ejecutando = False  

    def iniciar(self):
        while self.ejecutando:
            self.mostrar_opciones()
            opcion = input("Seleccione una opción: ")
            print(opcion)
            self.ejecutar_opcion(opcion)
menu = MenuConcreto()
menu.iniciar()

