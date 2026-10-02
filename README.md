Markdown

# Práctica UD1 - Restaurante PSP

**Nombre del alumno:** Jonay Velázquez Luis  
**Módulo:** Programación de Servicios y Procesos (2º DAM)  

---

## Descripción breve de la práctica
Esta práctica consiste en el desarrollo de una aplicación en Python para gestionar la comanda y preparación de platos en un restaurante utilizando concurrencia de subprocesos. Se implementa tanto la solución paso a paso de los ejercicios orientados a la gestión de procesos (`subprocess`), como una aplicación final interactiva que permite crear pedidos, monitorear la cocina y cancelar preparaciones en tiempo real sin bloquear el programa principal.

---

## Requisitos para ejecutar el proyecto
* **Python 3.8** o superior instalado.
* Sistema operativo compatible con ejecución de procesos (`Windows`, `Linux` o `macOS`).
* Terminal de comandos, PowerShell o la terminal integrada de VS Code.

---

## Estructura principal de archivos
```text
Jonay_Velazquez_Luis_Restaurante/
├── cocina/
│   ├── cocina.py
│   ├── cocina_error.py
│   ├── cocina_lenta.py
│   ├── cocina_pedido.py
│   ├── cocina_final.py
│   ├── hamburguesa.py
│   ├── pizza.py
│   └── postre.py
├── ejercicios/
│   ├── ejer1.py
│   ├── ejer02.py
│   ├── ejer3.py
│   ├── ejer4.py
│   ├── ejer5.py
│   ├── ejer6.py
│   ├── ejer7.py
│   ├── ejer8.py
│   └── ejer9.py
├── informe/
│   └── conexion.md
├── proyecto_final/
│   └── restaurante.py
├── README.md
└── .gitignore

Instrucciones para ejecutar restaurante.py

Para iniciar la aplicación interactiva del proyecto final, abre la terminal en la raíz del repositorio y ejecuta:
Bash

python proyecto_final/restaurante.py

Resumen de los conceptos de procesos utilizados

    subprocess.Popen(): Permite lanzar subprocesos en segundo plano de manera no bloqueante para mantener la fluidez de la interfaz del programa principal.

    PID (Process ID): Identificador único que asigna el sistema operativo a cada preparación para rastrear y gestionar su ejecución de forma individual.

    poll(): Permite consultar de forma no bloqueante si un proceso sigue ejecutándose (None) o si ya ha finalizado.

    wait(): Utilizado para sincronizar el cierre de subprocesos y asegurar la liberación de recursos del sistema.

    terminate(): Utilizado para cancelar y detener preparaciones activas a petición del usuario.

    PIPE y communicate(): Manejo de tuberías estándar (stdin, stdout, stderr) para la comunicación bidireccional de datos entre el proceso padre y el proceso hijo.

    TimeoutExpired y CalledProcessError: Gestión y control de excepciones en ejecuciones de procesos con tiempo límite o errores en ejecución.

Explicación del flujo de ramas empleado

Se ha utilizado una metodología GitFlow local-first:

    develop: Rama principal de desarrollo donde se van integrando las versiones probadas y estables.

    feature/ejerX / feature/proyecto-final: Ramas independientes creadas secuencialmente para trabajar cada ejercicio de manera aislada.

    Integración sin borrado: Una vez verificado el funcionamiento de cada ejercicio o parte del proyecto, los cambios se han fusionado mediante git merge dentro de develop, manteniendo la integridad de las ramas de características sin aplicar comandos de borrado explícito.