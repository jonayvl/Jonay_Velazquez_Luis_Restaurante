import sys
import time

if len(sys.argv) < 3:
    print("Error: Se requiere el nombre del plato y el tiempo.")
    sys.exit(1)

nombre_plato = sys.argv[1]
tiempo = int(sys.argv[2])

time.sleep(tiempo)
print(f"Plato completado: {nombre_plato}")