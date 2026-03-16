# Monitoreo del Sistema con Django y Psutil

**Autor:** Marcos Tulio Amador Rodriguez  
**Número de Cuenta:** 202010110449

## Descripción del Proyecto

Esta aplicación web con Django permite visualizar en tiempo real el estado del sistema, incluyendo el uso del CPU, la memoria RAM, el almacenamiento en disco y otros recursos relevantes, utilizando la librería externa psutil.

## Instalación y Ejecución

### Prerrequisitos

- Python 3.8 o superior
- Virtual environment (opcional pero recomendado)

### Pasos para Ejecutar el Proyecto Localmente

1. Clona o descarga el proyecto en tu máquina local.

2. Navega al directorio del proyecto:
   ```
   cd monitor
   ```

3. Crea y activa un entorno virtual:
   ```
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

4. Instala las dependencias:
   ```
   pip install -r requirements.txt
   ```

5. Ejecuta las migraciones:
   ```
   python manage.py migrate
   ```

6. Inicia el servidor de desarrollo:
   ```
   python manage.py runserver
   ```

7. Abre tu navegador y ve a `http://127.0.0.1:8000/` para ver la aplicación.

## Dependencias

- **Django**: Framework web para Python.
- **Psutil**: Librería para obtener información del sistema.

## Componentes

- **Vista (views.py)**: Contiene la lógica para recolectar datos del sistema usando psutil y renderizar la página principal.
- **Plantillas (templates)**: Página HTML que muestra los datos de forma estructurada en tarjetas.
- **URLs**: Configuración de rutas para acceder a la aplicación.

## Funcionalidades

- Muestra porcentaje de uso del CPU y número de núcleos.
- Información de memoria RAM (total, usado, porcentaje).
- Uso del disco duro (total, usado, libre, porcentaje).
- Información del sistema operativo.
- Botón para actualizar manualmente los datos.
- Actualización automática de la página cada 3 segundos usando JavaScript.

## Manejo de Errores

La aplicación maneja posibles errores si psutil no puede obtener un dato, mostrando un mensaje de error en la página.