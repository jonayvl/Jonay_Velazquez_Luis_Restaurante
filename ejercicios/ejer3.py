import subprocess
import sys

resultado = subprocess.run(
    [sys.executable, "cocina/cocina.py"],
    capture_output=True,
    text=True
)

print("===== INFORME DEL PEDIDO =====")
print("Mensaje de cocina:")
print(resultado.stdout.strip())

print("\nErrores:")
print(resultado.stderr.strip() if resultado.stderr.strip() else "(Sin errores)")

print("\nCódigo de retorno:")
print(resultado.returncode)