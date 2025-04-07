from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre_usuario):
        self.nombre_usuario = nombre_usuario

    @abstractmethod
    def autenticar(self, credencial):
        pass

class UsuarioCodigo(Usuario):
    def __init__(self, nombre_usuario, contraseña):
        super().__init__(nombre_usuario)
        self.contraseña = contraseña 
        
    def autenticar(self, credencial):
        return self.contraseña == credencial

# --- Ingreso de datos ---
nombre_usuario = input('Ingrese su nombre de usuario: ')
print(nombre_usuario)
contraseña = input('Ingrese su contraseña: ')
print(contraseña)


usuario1 = UsuarioCodigo(nombre_usuario, contraseña)

codigo_ingresado = input('Ingrese su código para autenticarse: ')
print(codigo_ingresado)

if usuario1.autenticar(codigo_ingresado):
    print(' Autenticación exitosa')
else:
    print(' Error: Código incorrecto')

