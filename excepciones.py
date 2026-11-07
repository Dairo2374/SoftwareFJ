# excepciones.py
# Módulo para las excepciones personalizadas del sistema


class ErrorSistemaFJ(Exception):
    """Clase base para todas las excepciones personalizadas de Software FJ."""

    pass


class ClienteInvalidoError(ErrorSistemaFJ):
    """Se lanza cuando los datos del cliente (como documento o nombre) son incorrectos."""

    pass


class ParametroFaltanteError(ErrorSistemaFJ):
    """Se lanza cuando a una operación le faltan datos obligatorios para ejecutarse."""

    pass


class ServicioNoDisponibleError(ErrorSistemaFJ):
    """Se lanza cuando se intenta operar con un servicio inactivo o mal configurado."""

    pass


class ReservaInvalidaError(ErrorSistemaFJ):
    """Se lanza cuando la lógica de la reserva falla (ej. fechas cruzadas, cálculos inconsistentes)."""

    pass
