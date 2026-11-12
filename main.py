# main.py
# Archivo principal para la ejecución del programa

from logger import log
from excepciones import (
    ClienteInvalidoError,
    ParametroFaltanteError,
    ReservaInvalidaError,
)
from entidades import Cliente
from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reservas import Reserva


def simular_operaciones():
    print("\n--- SISTEMA SOFTWARE FJ ---")
    print("-------------------------------------\n")

    lista_clientes = []
    lista_servicios = []

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

    print("\n>> Operación 4: Creación correcta de servicios y uso de Polimorfismo.")
    try:
        sala = ReservaSala("Sala Ada Lovelace", 50000, 10)
        equipo = AlquilerEquipo("Servidor Dell PowerEdge", 150000, "Cómputo Avanzado")
        asesoria = AsesoriaEspecializada(
            "Arquitectura en Python", 80000, "Desarrollo de Software"
        )

        lista_servicios.extend([sala, equipo, asesoria])

        # Iteramos usando polimorfismo (todos tienen mostrar_detalles, pero se comportan distinto)
        for s in lista_servicios:
            print(s.mostrar_detalles())
            log.info(f"Servicio creado: {s.nombre}")
    except Exception as e:
        log.error(f"Fallo al crear servicios: {e}")

    print("\n>> Operación 5: Creación incorrecta de un servicio (precio negativo).")
    try:
        sala_invalida = ReservaSala("Sala Errónea", -20000, 5)
    except ParametroFaltanteError as e:
        log.error(f"Operación 5 denegada - Parámetro de servicio inválido: {e}")
        print(f"Error capturado: {e}")

    print(
        "\n>> Operación 6: Prueba de Sobrecarga (Cálculo normal vs Cálculo con descuento)."
    )
    try:
        # Se cobra la sala por 4 horas sin parámetros extra
        costo_normal = sala.calcular_costo(4)
        print(f"Costo Sala (4h, sin descuento): ${costo_normal}")

        # Se cobra la sala por 4 horas con 19% IVA y 10% de descuento (Sobrecarga de parámetros)
        costo_especial = sala.calcular_costo(4, impuesto=0.19, descuento=0.10)
        print(f"Costo Sala (4h, IVA 19%, Dcto 10%): ${costo_especial}")
    except Exception as e:
        log.error(f"Error al calcular costos de sala: {e}")

    print("\n>> Operación 7: Polimorfismo en cálculo (Asesoría nivel experto).")
    try:
        # Aquí el polimorfismo brilla: calcular_costo en Asesoría funciona diferente a la Sala
        costo_asesoria = asesoria.calcular_costo(3, nivel_experto=True)
        print(f"Costo Asesoría (3 sesiones, Nivel Experto): ${costo_asesoria}")
    except Exception as e:
        log.error(f"Error al calcular costos de asesoría: {e}")

    # Asegurémonos de tener los objetos instanciados para las reservas (los sacamos de las pruebas anteriores)
    cliente_valido = Cliente("Dairo", "1020304050", "dairo@unad.edu.co")
    sala = ReservaSala("Sala Ada Lovelace", 50000, 10)
    equipo = AlquilerEquipo("Servidor Dell", 150000, "Cómputo")
    lista_reservas = []

    print("\n>> Operación 8: Procesamiento de una reserva EXITOSA (try/else/finally).")
    try:
        # Reservamos la sala por 3 horas con 5% de descuento
        reserva_1 = Reserva(cliente_valido, sala, 3, descuento=0.05)
        reserva_1.procesar_reserva()
        lista_reservas.append(reserva_1)
        print(reserva_1.mostrar_detalles())
    except ReservaInvalidaError as e:
        log.error(f"Error procesando reserva 1: {e}")

    print(
        "\n>> Operación 9: Reserva FALLIDA por servicio no disponible (Encadenamiento de excepciones)."
    )
    try:
        # Desactivamos el servicio intencionalmente
        equipo.disponible = False
        reserva_2 = Reserva(cliente_valido, equipo, 2)
        reserva_2.procesar_reserva()
    except ReservaInvalidaError as e:
        # Aquí verás cómo se captura la excepción encadenada
        print(f"Error capturado correctamente: {e}")
        # e.__cause__ contiene el ServicioNoDisponibleError original
        log.error(f"Fallo reserva 2: {e} | Causa original: {e.__cause__}")
        lista_reservas.append(reserva_2)

    print(
        "\n>> Operación 10: Reserva FALLIDA por valores inválidos (try/except/finally)."
    )
    try:
        # Volvemos a activar el equipo, pero pasamos una cantidad negativa de días
        equipo.disponible = True
        reserva_3 = Reserva(cliente_valido, equipo, -5)  # -5 días es inválido
        reserva_3.procesar_reserva()
    except ReservaInvalidaError as e:
        print(f"Error capturado correctamente: {e}")
        log.error(f"Fallo reserva 3: {e} | Causa original: {e.__cause__}")
        lista_reservas.append(reserva_3)

    print("\n--- RESUMEN FINAL ---")
    print(f"Total Clientes procesados: 1 (válido) + varios fallidos")
    print(f"Total Reservas creadas: {len(lista_reservas)}")
    for r in lista_reservas:
        print(f" - {r.mostrar_detalles()}")

    print("\nEl programa finalizó sus 10 operaciones de manera ESTABLE.")
    print("Revisa el archivo 'sistema.log' para ver la trazabilidad completa.")
    print("-------------------------------------\n")


# Punto de entrada del programa
if __name__ == "__main__":
    simular_operaciones()
