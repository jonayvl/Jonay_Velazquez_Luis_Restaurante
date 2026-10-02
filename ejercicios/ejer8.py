import subprocess
import sys
import os

ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cocina_lenta_path = os.path.join(ruta_base, "cocina", "cocina_lenta.py")

print("Preparación iniciada.")

# Lanzar proceso largo en segundo plano
proceso = subprocess.Popen([sys.executable, cocina_lenta_path])
print(f"PID: {proceso.pid}")

# Esperar la acción del usuario
input("Pulse ENTER para cancelar el pedido.\n")

print("Cancelando preparación...")
# Solicitar terminación del proceso
proceso.terminate()

# Esperar a que el proceso se cierre completamente y limpiar recursos
proceso.wait()

print("Preparación finalizada.")