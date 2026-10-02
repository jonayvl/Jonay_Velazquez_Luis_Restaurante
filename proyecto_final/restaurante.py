import subprocess
import sys
import os
import time

ruta_base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
cocina_script = os.path.join(ruta_base, "cocina", "cocina_final.py")

# Estructura para almacenar los pedidos
# Formato: { pid: {"plato": str, "proceso": Popen} }
pedidos = {}

def mostrar_menu():
    print("\n===================================")
    print("RESTAURANTE PSP")
    print("===================================")
    print("1. Crear pedido")
    print("2. Consultar cocina")
    print("3. Cancelar preparación")
    print("4. Ver pedidos terminados")
    print("5. Salir")

def crear_pedido():
    plato = input("Nombre del plato: ").strip()
    if not plato:
        print("El nombre del plato no puede estar vacío.")
        return

    try:
        tiempo = int(input("Tiempo: ").strip())
        if tiempo <= 0:
            print("El tiempo debe ser mayor a 0 segundos.")
            return
    except ValueError:
        print("Error: Debe introducir un número entero para el tiempo.")
        return

    # Crear el proceso en segundo plano
    proceso = subprocess.Popen([sys.executable, cocina_script, plato, str(tiempo)])
    
    pedidos[proceso.pid] = {
        "plato": plato,
        "proceso": proceso
    }

    print("\nPedido enviado a cocina.")
    print(f"Plato: {plato}")
    print(f"PID: {proceso.pid}")

def consultar_cocina():
    if not pedidos:
        print("\nNo hay pedidos registrados.")
        return

    print("\n===== ESTADO DE COCINA =====")
    for pid, info in pedidos.items():
        proceso = info["proceso"]
        plato = info["plato"]
        
        # Consultar estado con poll()
        if proceso.poll() is None:
            estado = "PREPARANDO"
        else:
            estado = "TERMINADA"
            
        print(f"PID {pid} | {plato} | {estado}")

def cancelar_preparacion():
    if not pedidos:
        print("\nNo hay pedidos registrados.")
        return

    try:
        pid = int(input("Solicita el PID: ").strip())
    except ValueError:
        print("Error: El PID debe ser un número entero.")
        return

    if pid not in pedidos:
        print("Error: No existe ningún pedido con ese PID.")
        return

    proceso = pedidos[pid]["proceso"]
    plato = pedidos[pid]["plato"]

    if proceso.poll() is None:
        print(f"Cancelando preparación de {plato} (PID {pid})...")
        proceso.terminate()
        proceso.wait()
        print("Preparación cancelada con éxito.")
    else:
        print(f"El pedido de {plato} (PID {pid}) ya había terminado.")

def ver_pedidos_terminados():
    terminados = [info for info in pedidos.values() if info["proceso"].poll() is not None]

    if not terminados:
        print("\nNo hay pedidos terminados aún.")
        return

    print("\n===== PEDIDOS TERMINADOS =====")
    for info in terminados:
        print(f"PID {info['proceso'].pid} | {info['plato']}")

def salir():
    activos = [info for info in pedidos.values() if info["proceso"].poll() is None]

    if activos:
        print(f"\nQuedan {len(activos)} preparación(es) activa(s).")
        respuesta = input("¿Desea cancelar todas las preparaciones pendientes antes de salir? (s/n): ").strip().lower()
        if respuesta == 's':
            for info in activos:
                print(f"Cancelando PID {info['proceso'].pid} ({info['plato']})...")
                info["proceso"].terminate()
                info["proceso"].wait()
            print("Todas las preparaciones pendientes han sido canceladas.")
    
    print("Saliendo del Restaurante PSP. ¡Hasta pronto!")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione opción: ").strip()

        if opcion == "1":
            crear_pedido()
        elif opcion == "2":
            consultar_cocina()
        elif opcion == "3":
            cancelar_preparacion()
        elif opcion == "4":
            ver_pedidos_terminados()
        elif opcion == "5":
            salir()
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    main()