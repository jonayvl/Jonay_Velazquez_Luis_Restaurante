import subprocess
import sys

print("--- 1. Ejecución con análisis manual de returncode ---")
resultado = subprocess.run(
    [sys.executable, "cocina/cocina_error.py"],
    capture_output=True,
    text=True
)

print(f"stdout: {resultado.stdout.strip()}")
print(f"stderr: {resultado.stderr.strip()}")
print(f"returncode: {resultado.returncode}")

if resultado.returncode != 0:
    print("ERROR: el pedido no ha podido prepararse.")

print("\n--- 2. Ejecución con check=True y captura de CalledProcessError ---")
try:
    subprocess.run(
        [sys.executable, "cocina/cocina_error.py"],
        check=True,
        capture_output=True,
        text=True
    )
except subprocess.CalledProcessError as e:
    print("ERROR: el pedido no ha podido prepararse.")
    print(f"Código devuelto por el subproceso: {e.returncode}")
    print(f"Mensaje de error capturado: {e.stderr.strip()}")