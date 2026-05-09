from Servicio import Servicio

class ReservaSala(Servicio):
    def __init__(self, nombre, precio_base, horas):
        super().__init__(nombre, precio_base)
        self.horas = horas

    def calcular_costo(self):
        return self.precio_base * self.horas

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


class AlquilerEquipo(Servicio):
    def __init__(self, nombre, precio_base, dias):
        super().__init__(nombre, precio_base)
        self.dias = dias

    def calcular_costo(self):
        return self.precio_base * self.dias

    def descripcion(self):
        return f"Alquiler de equipo por {self.dias} días"


class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre, precio_base, sesiones):
        super().__init__(nombre, precio_base)
        self.sesiones = sesiones

    def calcular_costo(self):
        return self.precio_base * self.sesiones

    def descripcion(self):
        return f"Asesoría especializada de {self.sesiones} sesiones"
