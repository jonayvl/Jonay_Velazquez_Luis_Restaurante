import subprocess
import sys
import os
import time

ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

hamburguesa_path = os.path.join(ruta_base, "cocina", "hamburguesa.py")
pizza_path = os.path.join(ruta_base, "cocina", "pizza.py")
postre_path = os.path.join(ruta_base, "cocina", "postre.py")

# Lanzar los procesos
p_hamburguesa = subprocess.Popen([sys.executable, hamburguesa_path])
p_pizza = subprocess.Popen([sys.executable, pizza_path])
p_postre = subprocess.Popen([sys.executable, postre_path])

platos = {
    "Hamburguesa": p_hamburguesa,
    "Pizza": p_pizza,
    "Postre": p_postre
}

# Bucle monitor mientras haya algún proceso en marcha
while True:
    print("===== ESTADO DE COCINA =====")
    activos = 0
    
    for nombre, proceso in platos.items():
        # poll() devuelve None si sigue en ejecución
        estado_codigo = proceso.poll()
        if estado_codigo is None:
            estado_texto = "PREPARANDO"
            activos += 1
        else:
            estado_texto = "TERMINADA"
        
        print(f"{nombre}: {estado_texto}")
    
    print("-" * 28)
    
    if activos == 0:
        break
        
    time.sleep(1)