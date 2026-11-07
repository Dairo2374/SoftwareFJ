# main.py
# Archivo principal para la ejecución del programa

from logger import log
from excepciones import ClienteInvalidoError


def simular_operaciones():
    print("\n--- SISTEMA SOFTWARE FJ ---")
    print("-------------------------------------\n")

    # Prueba de manejo de excepciones y log
    try:
        print("Intentando crear un cliente con documento vacío...")
        raise ClienteInvalidoError("El documento del cliente no puede estar vacío.")
    except ClienteInvalidoError as e:
        # Aquí capturamos el error específico y lo enviamos al archivo log
        log.error(f"Fallo en validación: {e}")
        print(
            "-> Error capturado con éxito. El programa no se detuvo (Revisa sistema.log)."
        )

    finally:
        log.info("Bloque de prueba de cliente finalizado.")

    print("\nEl programa sigue ejecutándose de forma estable.")
    print("-------------------------------------\n")


# Punto de entrada del programa
if __name__ == "__main__":
    simular_operaciones()
