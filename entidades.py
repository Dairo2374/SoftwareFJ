# entidades.py
# Módulo para las clases abstractas generales, Cliente y Reserva

from abc import ABC, abstractmethod
import uuid  # Librería nativa para generar identificadores únicos
from excepciones import ClienteInvalidoError, ParametroFaltanteError


class EntidadGeneral(ABC):
    """
    Clase abstracta que representa cualquier entidad del sistema.
    Implementa el principio de Abstracción.
    """

    def __init__(self):
        # Todo objeto en el sistema tendrá un identificador único protegido
        self._id = str(uuid.uuid4())[:8]

    @property
    def id(self):
        return self._id

    @abstractmethod
    def mostrar_detalles(self):
        """Método abstracto: obliga a las clases hijas a implementarlo."""
        pass


class Cliente(EntidadGeneral):
    """
    Clase Cliente con validaciones robustas y encapsulación.
    Hereda de EntidadGeneral.
    """

    def __init__(self, nombre, documento, correo):
        super().__init__()
        # Al asignar mediante self.nombre (sin los guiones),
        # Python invoca automáticamente los setters (las validaciones)
        self.nombre = nombre
        self.documento = documento
        self.correo = correo

    # --- INICIO DEL ENCAPSULAMIENTO Y VALIDACIONES ---

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ClienteInvalidoError("El nombre debe tener al menos 3 caracteres.")
        self.__nombre = valor.strip()

    @property
    def documento(self):
        return self.__documento

    @documento.setter
    def documento(self, valor):
        if not valor:
            raise ParametroFaltanteError("El documento es obligatorio.")
        if not isinstance(valor, str) or not valor.isdigit():
            raise ClienteInvalidoError("El documento debe contener únicamente números.")
        self.__documento = valor

    @property
    def correo(self):
        return self.__correo

    @correo.setter
    def correo(self, valor):
        if not valor or "@" not in valor:
            raise ClienteInvalidoError(
                "El correo electrónico no tiene un formato válido."
            )
        self.__correo = valor.strip()

    # Implementación obligatoria del método abstracto
    def mostrar_detalles(self):
        return f"Cliente [{self.id}]: {self.nombre} | Doc: {self.documento} | Correo: {self.correo}"
