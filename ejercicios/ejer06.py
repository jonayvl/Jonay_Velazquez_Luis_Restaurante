import subprocess
import sys
import os
import time

ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


hamburguesa_path = os.path.join(ruta_base, "cocina", "hamburguesa.py")
pizza_path = os.path.join(ruta_base, "cocina", "pizza.py")
postre_path = os.path.join(ruta_base, "cocina", "postre.py")

print("PEDIDO #001")
inicio = time.time()

p1 = subprocess.Popen([sys.executable, hamburguesa_path])
print(f"Hamburguesa enviada a cocina. PID: {p1.pid}")

p2 = subprocess.Popen([sys.executable, pizza_path])
print(f"Pizza enviada a cocina. PID: {p2.pid}")

p3 = subprocess.Popen([sys.executable, postre_path])
print(f"Postre enviado a cocina. PID: {p3.pid}")

p1.wait()
p2.wait()
p3.wait()

fin = time.time()
print(f"\nTodos los platos han finalizado en {fin - inicio:.2f} segundos.")