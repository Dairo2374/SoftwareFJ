# main.py
# Archivo principal para la ejecución del programa

from logger import log
from excepciones import ClienteInvalidoError, ParametroFaltanteError
from entidades import Cliente

from servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada


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

    print("\n-------------------------------------\n")


# Punto de entrada del programa
if __name__ == "__main__":
    simular_operaciones()
