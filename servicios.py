# servicios.py
# Módulo para la clase abstracta Servicio y sus clases derivadas

from abc import abstractmethod
from entidades import EntidadGeneral
from excepciones import ParametroFaltanteError, ServicioNoDisponibleError


class Servicio(EntidadGeneral):
    """
    Clase abstracta base para todos los servicios de Software FJ.
    Hereda de EntidadGeneral para obtener el ID automático.
    """

    def __init__(self, nombre, precio_base):
        super().__init__()
        if not nombre or precio_base < 0:
            raise ParametroFaltanteError(
                "El nombre del servicio es obligatorio y el precio no puede ser negativo."
            )
        self.nombre = nombre
        self.precio_base = precio_base
        self.disponible = True  # Atributo de estado

    # Implementamos el método abstracto de la clase EntidadGeneral
    def mostrar_detalles(self):
        estado = "Disponible" if self.disponible else "No Disponible"
        return f"[{self.id}] {self.describir_servicio()} | Precio Base: ${self.precio_base} | Estado: {estado}"

    @abstractmethod
    def calcular_costo(self):
        """Método polimórfico que cada servicio hijo debe implementar."""
        pass

    @abstractmethod
    def describir_servicio(self):
        """Método abstracto para detallar la naturaleza del servicio."""
        pass


# --- CLASES HIJAS (HERENCIA Y POLIMORFISMO) ---


class ReservaSala(Servicio):
    def __init__(self, nombre, precio_base, capacidad):
        super().__init__(nombre, precio_base)
        self.capacidad = capacidad

    # SOBRECARGA: parámetros opcionales (impuesto y descuento)
    def calcular_costo(self, horas, impuesto=0.0, descuento=0.0):
        if horas <= 0:
            raise ValueError("Las horas de reserva deben ser mayores a cero.")
        subtotal = self.precio_base * horas
        total = subtotal - (subtotal * descuento) + (subtotal * impuesto)
        return total

    def describir_servicio(self):
        return (
            f"Sala de Reuniones '{self.nombre}' (Capacidad: {self.capacidad} personas)"
        )


class AlquilerEquipo(Servicio):
    def __init__(self, nombre, precio_base, tipo_equipo):
        super().__init__(nombre, precio_base)
        self.tipo_equipo = tipo_equipo

    # SOBRECARGA: el alquiler puede incluir un seguro_adicional que por defecto es 0
    def calcular_costo(self, dias, seguro_adicional=0.0, impuesto=0.0, descuento=0.0):
        if dias <= 0:
            raise ValueError("Los días de alquiler deben ser mayores a cero.")
        subtotal = (self.precio_base * dias) + seguro_adicional
        total = subtotal - (subtotal * descuento) + (subtotal * impuesto)
        return total

    def describir_servicio(self):
        return f"Alquiler de Equipo de {self.tipo_equipo} '{self.nombre}'"


class AsesoriaEspecializada(Servicio):
    def __init__(self, nombre, precio_base, tema):
        super().__init__(nombre, precio_base)
        self.tema = tema

    # SOBRECARGA: parámetro booleano para recargo por nivel experto
    def calcular_costo(
        self, sesiones, nivel_experto=False, impuesto=0.0, descuento=0.0
    ):
        if sesiones <= 0:
            raise ValueError("El número de sesiones debe ser mayor a cero.")

        # Si requiere un ingeniero experto, el precio base sube un 30%
        multiplicador_experto = 1.30 if nivel_experto else 1.0
        subtotal = self.precio_base * sesiones * multiplicador_experto
        total = subtotal - (subtotal * descuento) + (subtotal * impuesto)
        return total

    def describir_servicio(self):
        return f"Asesoría en {self.tema} - '{self.nombre}'"
