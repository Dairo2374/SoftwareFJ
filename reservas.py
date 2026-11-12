# reservas.py
from entidades import EntidadGeneral, Cliente
from servicios import Servicio
from excepciones import ReservaInvalidaError, ServicioNoDisponibleError
from logger import log


class Reserva(EntidadGeneral):
    """
    Clase que gestiona la relación entre un Cliente y un Servicio.
    Implementa el manejo avanzado de excepciones requerido en el proyecto.
    """

    def __init__(self, cliente, servicio, cantidad, **parametros_extra):
        super().__init__()

        # Validación de tipos
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("El cliente proporcionado no es válido.")
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("El servicio proporcionado no es válido.")

        self.cliente = cliente
        self.servicio = servicio
        self.cantidad = cantidad  # Puede ser horas, días, o sesiones
        self.parametros_extra = parametros_extra  # Recibe impuesto, descuento, etc.
        self.estado = "Pendiente"
        self.costo_total = 0.0

    def procesar_reserva(self):
        """
        Método central que aplica try / except / else / finally
        y encadenamiento de excepciones.
        """
        log.info(
            f"Iniciando procesamiento de reserva {self.id} para {self.cliente.nombre}"
        )

        try:
            # 1. Verificar que el servicio esté disponible
            if not self.servicio.disponible:
                raise ServicioNoDisponibleError(
                    f"El servicio '{self.servicio.nombre}' está fuera de servicio."
                )

            # 2. Intentar calcular el costo (aquí se invoca el polimorfismo)
            # Si 'cantidad' es negativo, calcular_costo lanzará un ValueError
            self.costo_total = self.servicio.calcular_costo(
                self.cantidad, **self.parametros_extra
            )

        except ServicioNoDisponibleError as error_original:
            self.estado = "Cancelada (Servicio no disponible)"
            # ENCADENAMIENTO DE EXCEPCIONES: Lanzamos ReservaInvalidaError a partir del error original
            raise ReservaInvalidaError(
                f"Fallo al procesar reserva {self.id}."
            ) from error_original

        except ValueError as error_original:
            self.estado = "Cancelada (Datos de cálculo inválidos)"
            # ENCADENAMIENTO DE EXCEPCIONES
            raise ReservaInvalidaError(
                f"Parámetros numéricos inválidos en reserva {self.id}."
            ) from error_original

        except Exception as error_original:
            self.estado = "Cancelada (Error Inesperado)"
            raise ReservaInvalidaError(
                "Ocurrió un error catastrófico no previsto."
            ) from error_original

        else:
            # BLOQUE ELSE: Se ejecuta SOLO si el bloque try terminó sin lanzar ninguna excepción
            self.estado = "Confirmada"
            print(f" -> ÉXITO: Reserva procesada. Total a pagar: ${self.costo_total}")

        finally:
            # BLOQUE FINALLY: Se ejecuta SIEMPRE, haya fallado o sido exitosa
            log.info(
                f"Proceso de reserva {self.id} concluido. Estado final: {self.estado}"
            )

    def mostrar_detalles(self):
        return (
            f"Reserva [{self.id}] | Cliente: {self.cliente.nombre} | "
            f"Servicio: {self.servicio.nombre} | Estado: {self.estado} | Total: ${self.costo_total}"
        )
