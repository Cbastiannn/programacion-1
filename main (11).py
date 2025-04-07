class Cuenta:
    def __init__(self, nombre_usuario, contraseña):
        self.__nombre_usuario = nombre_usuario  # Atributos privados
        self.__contraseña = contraseña

    # Método para validar el acceso
    def autenticar(self, nombre_intento, contraseña_intento):
        return self.__nombre_usuario == nombre_intento and self.__contraseña == contraseña_intento

    # Método para cambiar la contraseña (opcional)
    def cambiar_contraseña(self, nueva_contraseña):
        if len(nueva_contraseña) >= 6:
            self.__contraseña = nueva_contraseña
            return " Contraseña actualizada correctamente."
        else:
            return " La contraseña debe tener al menos 6 caracteres."

    # Mostrar usuario (no la contraseña)
    def get_usuario(self):
        return self.__nombre_usuario


# --- Crear cuenta ---
nombre = input(' Ingrese su nombre de usuario: ')
clave = input(' Ingrese su contraseña: ')

cuenta = Cuenta(nombre, clave)

# --- Intentar autenticación ---
print("\n--- Inicio de sesión ---")
nombre_login = input(' Usuario: ')
clave_login = input(' Contraseña: ')

if cuenta.autenticar(nombre_login, clave_login):
    print(f'Bienvenido/a, {cuenta.get_usuario()}')
else:
    print(' Usuario o contraseña incorrecta')

# --- Intentar cambio de contraseña ---
print("\n--- Cambiar contraseña ---")
nueva_clave = input('Ingrese una nueva contraseña: ')
print(cuenta.cambiar_contraseña(nueva_clave))

# --- Nuevo intento de autenticación ---
print("\n--- Nuevo intento de inicio de sesión ---")
clave_login2 = input(' Ingrese la nueva contraseña: ')
if cuenta.autenticar(nombre_login, clave_login2):
    print(' Acceso con nueva contraseña')
else:
    print('Contraseña incorrecta')
