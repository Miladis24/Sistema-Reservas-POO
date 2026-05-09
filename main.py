from cliente import Cliente
from servicios_especificos import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva

print("===== SISTEMA DE GESTIÓN =====")

# OPERACIÓN 1
try:
    cliente1 = Cliente("Miladis", "12345", "miladis@gmail.com")
    print(cliente1.obtener_datos())
except Exception as e:
    print(e)

# OPERACIÓN 2
try:
    cliente2 = Cliente("", "54321", "correo_invalido")
except Exception as e:
    print(f"Error detectado: {e}")

# OPERACIÓN 3
servicio1 = ReservaSala("Sala Premium", 50000, 3)

# OPERACIÓN 4
servicio2 = AlquilerEquipo("Portátil", 80000, 2)

# OPERACIÓN 5
servicio3 = AsesoriaEspecializada("Asesoría Python", 100000, 4)

# OPERACIÓN 6
reserva1 = Reserva(cliente1, servicio1, 3)
reserva1.confirmar()
reserva1.mostrar_reserva()

# OPERACIÓN 7
reserva2 = Reserva(cliente1, servicio2, 2)
reserva2.confirmar()
reserva2.mostrar_reserva()

# OPERACIÓN 8
reserva3 = Reserva(cliente1, servicio3, 4)
reserva3.confirmar()
reserva3.mostrar_reserva()

# OPERACIÓN 9
reserva_error = Reserva(cliente1, servicio1, -1)
reserva_error.confirmar()

# OPERACIÓN 10
reserva1.cancelar()
reserva1.cancelar()

print("===== FIN DEL SISTEMA =====")
