import os
import sys
import subprocess
from datetime import datetime

# -------------------------------
# CONFIGURACIÓN DE REPORTES
# -------------------------------
REPORTS_DIR = os.path.join(os.getcwd(), "reports", "behave")
os.makedirs(REPORTS_DIR, exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
REPORT_FILE = os.path.join(REPORTS_DIR, f"behave_report_{timestamp}.html")

# -------------------------------
# EJECUCIÓN DE BEHAVE
# -------------------------------
def run_behave():
    print(" Ejecutando tests BDD con Behave…")

    behave_cmd = [
        "behave",
        f"--format=behave_html_formatter:HTMLFormatter",
        f"--outfile={REPORT_FILE}",
        "--no-capture"
    ]

    try:
        result = subprocess.run(behave_cmd, text=True)

        if result.returncode == 0:
            print(f" Tests completados correctamente.")
        else:
            print(f" Algunos tests fallaron.")

        print(f" Reporte generado en: {REPORT_FILE}")

    except FileNotFoundError:
        print(" ERROR: Behave no está instalado.")
        print("Instalalo con: pip install behave behave-html-formatter")

    except Exception as e:
        print(f"Error ejecutando Behave: {e}")


if __name__ == "__main__":
    run_behave()
