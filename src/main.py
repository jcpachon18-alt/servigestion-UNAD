from excepciones import (
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaError
)

print("========== INICIO DEL SISTEMA ==========\n")


# ---------------------------------------------------
# PRUEBA 1: Validación de cliente
# ---------------------------------------------------

try:
    print("Verificando información del cliente...")
    raise ClienteInvalidoError()

except ClienteInvalidoError as error:
    print(f"Se detectó un problema: {error}")

else:
    print("Cliente registrado correctamente.")

finally:
    print("Finalizó la validación del cliente.\n")


# ---------------------------------------------------
# PRUEBA 2: Validación de servicio
# ---------------------------------------------------

try:
    print("Consultando disponibilidad del servicio...")
    raise ServicioNoDisponibleError()

except ServicioNoDisponibleError as error:
    print(f"Se detectó un problema: {error}")

finally:
    print("Finalizó la validación del servicio.\n")


# ---------------------------------------------------
# PRUEBA 3: Procesamiento de reserva
# ---------------------------------------------------

try:
    print("Procesando reserva...")
    raise ReservaError()

except ReservaError as error:
    print(f"Se detectó un problema: {error}")

finally:
    print("Finalizó el procesamiento de la reserva.\n")


print("========== EL SISTEMA SIGUE FUNCIONANDO ==========")
