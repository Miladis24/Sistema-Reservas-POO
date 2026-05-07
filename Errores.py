class ErrorReserva(Exception):
    """Excepción para errores en reservas"""
    pass


class ClienteInvalidoError(Exception):
    """Excepción para clientes inválidos"""
    pass


class ServicioNoDisponibleError(Exception):
    """Excepción para servicios no disponibles"""
    pass
