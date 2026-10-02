import subprocess
import sys

print("Pedido recibido.")
print("Enviando pedido a cocina...")

# Lanza cocina/cocina.py y espera a que termine
subprocess.run([sys.executable, "cocina/cocina.py"], check=True)

print("Pedido preparado.")