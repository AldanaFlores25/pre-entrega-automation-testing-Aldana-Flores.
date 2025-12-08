import logging
import pathlib

# Crear (si no existe) la carpeta donde se guardarán los logs
audit_dir = pathlib.Path('logs')
audit_dir.mkdir(exist_ok=True)

# Definir el archivo de log dentro de la carpeta creada
log_file = audit_dir / 'suite.log'

# Crear un logger con nombre "Automation_TalentoTech"
logger = logging.getLogger("Automation_TalentoTech")

# Configurar el nivel mínimo que registrará el logger (INFO)
logger.setLevel(logging.INFO)

# Evitar agregar múltiples handlers si el logger ya tiene uno
if not logger.handlers:
    # Crear un manejador de archivo, modo append para no sobrescribir logs anteriores
    file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")

    # Definir formato del mensaje del log
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Asociar el formato al handler
    file_handler.setFormatter(formatter)

    # Agregar el handler al logger principal
    logger.addHandler(file_handler)