from excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaError
)


print("=== INICIO DEL SISTEMA ===")


# PRUEBA 1: Error de cliente
try:
    raise ClienteInvalidoError()

except ClienteInvalidoError as error:
    print(f"Error detectado: {error}")


# PRUEBA 2: Error de servicio
try:
    raise ServicioNoDisponibleError()

except ServicioNoDisponibleError as error:
    print(f"Error detectado: {error}")


# PRUEBA 3: Error de reserva
try:
    raise ReservaError()

except ReservaError as error:
    print(f"Error detectado: {error}")


print("=== EL SISTEMA SIGUE FUNCIONANDO ===")
