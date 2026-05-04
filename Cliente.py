class Cliente:
    def __init__(self, nombre, documento, correo):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        if not documento:
            raise ValueError("El documento no puede estar vacío")
        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.__nombre = nombre
        self.__documento = documento
        self.__correo = correo

    def obtener_datos(self):
        return f"Cliente: {self.__nombre}, Documento: {self.__documento}, Correo: {self.__correo}"
