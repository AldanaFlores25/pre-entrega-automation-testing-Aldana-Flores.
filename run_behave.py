# run_behave.py
import subprocess
import os

print("Ejecutando tests BDD con Behave…")

# aseguramos carpeta del reporte
os.makedirs("reports/behave", exist_ok=True)

result = subprocess.run([
    "behave",
    "-f", "html",
    "-o", "reports/behave/behave_report.html"
])

if result.returncode != 0:
    print("❌ Algunos tests BDD fallaron")
    exit(result.returncode)

print("✅ Tests BDD finalizados correctamente")
