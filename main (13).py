class SelectorOpciones:
    def __init__(self):
        self.__opciones = ["Encender", "Apagar", "Reiniciar"]
        self.__opcion_actual = self.__opciones[0]  # Por defecto: Encender

    def set_opcion(self, opcion):
        if opcion in self.__opciones:
            self.__opcion_actual = opcion
        else:
            print("⚠️ Opción inválida. Las opciones válidas son:", self.__opciones)

    def get_opcion(self):
        return self.__opcion_actual

    def mostrar_opciones(self):
        print("Opciones disponibles:")
        for i, opcion in enumerate(self.__opciones, 1):
            print(f"{i}. {opcion}")

    def ejecutar_accion(self):
        if self.__opcion_actual == "Encender":
            print("🔌 El sistema se está encendiendo...")
        elif self.__opcion_actual == "Apagar":
            print("⛔ El sistema se está apagando...")
        elif self.__opcion_actual == "Reiniciar":
            print("🔄 El sistema se está reiniciando...")
        else:
            print("❌ Acción no reconocida.")


# --- Uso interactivo ---
selector = SelectorOpciones()

while True:
    print("\n--- MENÚ DE OPCIONES ---")
    selector.mostrar_opciones()
    opcion_num = input("Seleccione una opción (1-3) o escriba 'salir' para terminar: ")

    if opcion_num.lower() == "salir":
        print("👋 Programa finalizado.")
        break

    if opcion_num.isdigit():
        indice = int(opcion_num) - 1
        if 0 <= indice < 3:
            opcion_elegida = selector._SelectorOpciones__opciones[indice]  # Accedemos al atributo privado
            selector.set_opcion(opcion_elegida)
            print(f"\n➡️ Opción seleccionada: {selector.get_opcion()}")
            selector.ejecutar_accion()
        else:
            print("❌ Número fuera de rango. Elija entre 1 y 3.")
    else:
        print("❌ Entrada inválida. Por favor, ingrese un número o 'salir'.")
