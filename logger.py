# logger.py
# Módulo para la configuración del registro de eventos y errores (Logs)

import logging

# Configuración general del registro de eventos
logging.basicConfig(
    filename="sistema.log",  # Archivo donde se guardará el historial
    filemode="a",  # 'a' (append) para no borrar el historial anterior
    level=logging.INFO,  # Captura desde mensajes informativos hasta errores críticos
    format="%(asctime)s - [%(levelname)s] - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Instancia del logger que importaremos en los demás archivos
log = logging.getLogger("SoftwareFJ")
