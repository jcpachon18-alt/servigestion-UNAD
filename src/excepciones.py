from datetime import datetime


# Función para registrar errores en logs.txt
def registrar_log(mensaje):
    with open("logs.txt", "a", encoding="utf-8") as archivo:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        archivo.write(f"[{fecha}] {mensaje}\n")


# Clase base para excepciones del sistema
class SistemaGestionError(Exception):
    pass


# Excepción para clientes inválidos
class ClienteInvalidoError(SistemaGestionError):
    def __init__(self, mensaje="Datos del cliente no válidos"):
        registrar_log(mensaje)
        super().__init__(mensaje)


# Excepción para servicios no disponibles
class ServicioNoDisponibleError(SistemaGestionError):
    def __init__(self, mensaje="Servicio no disponible"):
        registrar_log(mensaje)
        super().__init__(mensaje)


# Excepción para errores de reserva
class ReservaError(SistemaGestionError):
    def __init__(self, mensaje="Error en la reserva"):
        registrar_log(mensaje)
        super().__init__(mensaje)
