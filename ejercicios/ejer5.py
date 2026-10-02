import subprocess
import sys

try:
    subprocess.run(
        [sys.executable, "cocina/cocina_lenta.py"],
        timeout=5,
        capture_output=True,
        text=True
    )
except subprocess.TimeoutExpired:
    print("ERROR: el tiempo máximo de preparación ha sido superado.")
    print("Pedido cancelado.")