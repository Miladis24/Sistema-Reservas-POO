from errores import ErrorReserva
from logger import registrar_error, registrar_evento

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            if self.duracion <= 0:
                raise ErrorReserva("La duración debe ser mayor a cero")

            self.estado = "Confirmada"
            registrar_evento("Reserva confirmada correctamente")

        except ErrorReserva as e:
            registrar_error(str(e))
            print(f"Error al confirmar reserva: {e}")

    def cancelar(self):
        try:
            if self.estado == "Cancelada":
                raise ErrorReserva("La reserva ya está cancelada")

            self.estado = "Cancelada"
            registrar_evento("Reserva cancelada correctamente")

        except ErrorReserva as e:
            registrar_error(str(e))
            print(f"Error al cancelar reserva: {e}")

    def mostrar_reserva(self):
        print("===== RESERVA =====")
        print(self.cliente.obtener_datos())
        print(self.servicio.descripcion())
        print(f"Costo: ${self.servicio.calcular_costo()}")
        print(f"Estado: {self.estado}")
