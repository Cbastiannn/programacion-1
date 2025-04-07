class Factura: 
    def __init__(self, producto):
        self.__producto = producto
        self.__cantidad_producto = 1
        self.__valor_producto = 0

    def set_cantidad_producto(self, cantidad_producto):
        if cantidad_producto > 0: 
            self.__cantidad_producto = cantidad_producto
        else:
            print('Número de compra inválido, debe ser mayor que cero.')
   
    def get_cantidad_producto(self):
        return self.__cantidad_producto

    def set_valor_producto(self, valor):
        if valor > 0:
            self.__valor_producto = valor
        else:
            print('El valor del producto debe ser mayor que cero.')

    def get_valor_producto(self):
        return self.__valor_producto

    def calcular_total(self):
        return self.__cantidad_producto * self.__valor_producto

    def mostrar_resumen(self):
        return f"Producto: {self.__producto} , Cantidad: {self.__cantidad_producto} , Valor unitario: ${self.__valor_producto:.2f} , Total: ${self.calcular_total():.2f}"


# Clase Cliente que usa la clase Factura
class Cliente:
    def __init__(self, producto, cantidad, valor):
        self.factura = Factura(producto)
        self.factura.set_cantidad_producto(cantidad)
        self.factura.set_valor_producto(valor)

    def calcular_compra(self):
        return self.factura.calcular_total()

    def mostrar_factura(self):
        return self.factura.mostrar_resumen()


# Entrada de datos
n_producto = input('Ingrese el nombre del producto: ')
cantidad_productos = int(input('¿Cuántos compró?: '))
valor_productos = int(input('Ingrese el valor de los productos: '))

# Crear cliente y calcular total
mi_cliente = Cliente(n_producto, cantidad_productos, valor_productos)
total = mi_cliente.calcular_compra()

print(f"\nResumen de compra:")
print(mi_cliente.mostrar_factura())

