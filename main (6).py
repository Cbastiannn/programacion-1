from abc import ABC, abstractmethod

class Factura(ABC): 
    def __init__(self, producto, cantidad_producto, valor_producto):
        self.producto = producto
        self.cantidad_producto = cantidad_producto
        self.valor_producto = valor_producto
        
    @abstractmethod
    def calcular_compra(self):
        pass

class Cliente(Factura):
    def calcular_compra(self):
        return self.cantidad_producto * self.valor_producto

# Solicitar datos al usuario
n_producto = input('Ingrese el nombre del producto: ')
print(n_producto)
cantidad_productos = int(input('¿Cuántos compró?: '))
print(cantidad_productos)
valor_productos = int(input('Ingrese el valor de los productos: '))
print(valor_productos)

mi_cliente = Cliente(n_producto, cantidad_productos, valor_productos)
total = mi_cliente.calcular_compra()

print(f"El total de la compra fue: {total}")
