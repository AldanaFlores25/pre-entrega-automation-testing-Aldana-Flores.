import subprocess

print("Ejecutando tests BDD con Behave…")
subprocess.run([
    "behave",
    "-f", "html",
    "-o", "reports/behave/behave_report.html"
])
