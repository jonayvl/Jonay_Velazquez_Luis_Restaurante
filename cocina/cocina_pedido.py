import sys

# Leer la comanda enviada por entrada estándar
pedido = sys.stdin.read().strip()

if pedido:
    print(f"Preparación completada: {pedido}")
else:
    print("Error: No se ha recibido ningún pedido.", file=sys.stderr)