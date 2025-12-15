# run_behave.py
import subprocess
import os
import sys

print("Ejecutando tests BDD con Behave…")

# asegurar carpeta
os.makedirs("reports/behave", exist_ok=True)

result = subprocess.run([
    "behave",
    "-f", "behave_html_formatter:HTMLFormatter",
    "-o", "reports/behave/behave_report.html"
])

if result.returncode != 0:
    print(" Algunos tests BDD fallaron")
    sys.exit(result.returncode)

print(" Tests BDD finalizados correctamente")
