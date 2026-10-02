import subprocess
import sys
import os

ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cocina_pedido_path = os.path.join(ruta_base, "cocina", "cocina_pedido.py")

plato = "Pizza carbonara"
print(f"Sistema envía:\n{plato}\n")

proceso = subprocess.Popen(
    [sys.executable, cocina_pedido_path],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

stdout, stderr = proceso.communicate(input=plato)

print(f"Cocina responde:\n{stdout.strip()}")