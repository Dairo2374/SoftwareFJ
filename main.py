# main.py
# Archivo principal para la ejecución del programa

from logger import log
from excepciones import ClienteInvalidoError, ParametroFaltanteError
from entidades import Cliente


def simular_operaciones():
    print("\n--- SISTEMA SOFTWARE FJ ---")
    print("-------------------------------------\n")

    lista_clientes = []

    print(">> Operación 1: Registro de un cliente válido.")
    try:
        cliente_valido = Cliente("Dairo", "1020304050", "dairo@unad.edu.co")
        lista_clientes.append(cliente_valido)
        print(cliente_valido.mostrar_detalles())
        log.info(f"Cliente creado exitosamente: {cliente_valido.id}")
    except Exception as e:
        log.error(f"Fallo inesperado: {e}")

    print("\n>> Operación 2: Intento de registro con documento inválido (letras).")
    try:
        cliente_invalido_1 = Cliente("Carlos", "102030ABC", "carlos@correo.com")
    except ClienteInvalidoError as e:
        log.error(f"Operación 2 denegada - Validación de Cliente: {e}")
        print(f"Error capturado: {e}")

    print(
        "\n>> Operación 3: Intento de registro con parámetro faltante (correo vacío)."
    )
    try:
        cliente_invalido_2 = Cliente("Ana", "987654321", "")
    except ClienteInvalidoError as e:
        log.error(f"Operación 3 denegada - Validación de Cliente: {e}")
        print(f"Error capturado: {e}")
    except ParametroFaltanteError as e:
        log.error(f"Operación 3 denegada - Parámetro faltante: {e}")
        print(f"Error capturado: {e}")

    print("\nResumen de clientes registrados en memoria:", len(lista_clientes))
    print("\nRevisa el archivo sistema.log para verificar la auditoría de errores.")
    print("-------------------------------------\n")


# Punto de entrada del programa
if __name__ == "__main__":
    simular_operaciones()
