import logging

logging.basicConfig(
    filename='sistema.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def registrar_error(mensaje):
    logging.error(mensaje)


def registrar_evento(mensaje):
    logging.warning(mensaje)
