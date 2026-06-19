# Sistema de Gestión de Licencias - Chatbot Administrativo

Este proyecto es un Trabajo Práctico Integrador (TPI) desarrollado para la cátedra de **Organización Empresarial** (TUPaD - UTN). Consiste en la automatización de un proceso administrativo (Solicitud de Licencias) mediante un Chatbot basado en una arquitectura de **Máquina de Estados Finito (FSM)**.

El sistema permite a los empleados de una organización gestionar sus días libres, vacaciones y justificar licencias de manera interactiva, validando las reglas de negocio en tiempo real y persistiendo la información en bases de datos simuladas (archivos CSV).

## 🚀 Características Principales

- **Arquitectura Basada en Estados:** El flujo de la conversación está gobernado por un diccionario de estado, lo que otorga "memoria" al trámite y permite saber exactamente en qué etapa se encuentra el usuario.
- **Gestión de Sesiones Incompletas:** Si un empleado abandona el trámite por la mitad, el sistema guarda su progreso. Al volver a ingresar con su DNI, el bot le preguntará si desea retomar desde donde lo dejó o iniciar uno nuevo.
- **Manejo del "Camino Infeliz" (Unhappy Path):** El usuario puede escribir la palabra `salir` o `cancelar` en _cualquier_ momento del proceso. El sistema interceptará la orden, guardará el progreso actual y cerrará el programa de forma segura.
- **Reglas de Negocio Automatizadas:** \* Verificación de saldo de días disponibles.
  - Validación de fechas (las solicitudes deben hacerse con al menos 15 días hábiles de anticipación).
  - Control de longitud de caracteres para textos justificativos.
- **Persistencia de Datos:** Lectura y escritura en archivos CSV separados por responsabilidad (empleados, solicitudes y sesiones pendientes).

## 📂 Estructura del Proyecto

El código está estructurado de manera modular para separar las responsabilidades, facilitando su escalabilidad y mantenimiento:

```text
📦 TPI-Organizacion-Empresarial
 ┣ 📂 data/
 ┃ ┣ 📜 datos_empleados.csv       # Base de datos de personal y días disponibles
 ┃ ┣ 📜 solicitudes_dias.csv      # Registro histórico de licencias generadas
 ┃ ┗ 📜 sesiones_pendientes.csv   # Memoria temporal de trámites inconclusos
 ┣ 📜 main.py                     # Punto de entrada y bucle principal del programa
 ┣ 📜 maquina_estados.py          # Enrutador central y funciones manejadoras de cada etapa
 ┣ 📜 validaciones.py             # Reglas lógicas, matemáticas, control de fechas y salidas seguras
 ┣ 📜 archivos.py                 # Módulo de persistencia (Lectura/Escritura de CSVs)
 ┣ 📜 solicitudes.py              # Empaquetado y generación final de la solicitud
 ┗ 📜 README.md                   # Documentación del proyecto


 ⚙️ Requisitos e Instalación
El proyecto está desarrollado en Python 3.x y utiliza únicamente bibliotecas de la biblioteca estándar (csv, os, datetime, sys). No es necesario instalar dependencias externas ni entornos virtuales complejos.

Clonar el repositorio:

Bash
git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)

Navegar al directorio del proyecto:

Bash
cd tu-repositorio
Ejecutar el chatbot:

Bash
python main.py


📖 Manual de Usuario
Ingreso: Al ejecutar el script, el sistema te dará la bienvenida y te solicitará tu DNI (sin puntos). El DNI debe existir previamente en el archivo data/datos_empleados.csv.

Trámites Pendientes: Si tenías una solicitud a medio cargar, el bot lo detectará automáticamente y te dará la opción de retomarla o descartarla.

Navegación: Selecciona las opciones del menú ingresando el número correspondiente (ej: 1 para Iniciar solicitud).

Fechas: Al ingresar la fecha de tu licencia, asegúrate de usar el formato DD/MM/YYYY. El sistema calculará automáticamente si cumple con los 15 días hábiles reglamentarios exigidos por RRHH.

Confirmación: Antes de generar el ticket final, el sistema te mostrará un resumen detallado. Si lo confirmas, se guardará en solicitudes_dias.csv y se limpiará tu sesión temporal.

Salir: Podés escribir salir en cualquier prompt (cuando el sistema te pida ingresar datos). Tu trámite quedará pausado y guardado automáticamente.

👥 Autores
Oliverio Arce - Desarrollador / Analista de Procesos

Marcos Magnello - Desarrollador / Analista de Procesos

Proyecto académico desarrollado para la Universidad Tecnológica Nacional (UTN).
```
