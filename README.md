# SIF2TXTASCII
Este script en Python permite convertir de forma automática archivos en formato SIF (.sif) a TXT (.txt) y ASCII (.asc).

Aplicación sencilla en Python para convertir archivos SIF (.sif) a formato TXT (.txt) y ASCII (.asc) mediante una interfaz gráfica para seleccionar la carpeta origen.

## 🔧 Requisitos

- Python ≥ 3.8
- sif-parser
- numpy
- tkinter (usually included with standard Python distributions)

Para instalar las librerías necesarias, ejecuta en tu terminal (bash, PowerShell o CMD):

```bash
pip install numpy
```
```bash
pip install sif-parser
```
Si quieres instalar todos los requisitos de una vez:

```bash
python -m pip install numpy sif-parser
```
## Descripción del script

El script abre una ventana típica de selección de carpeta para que el usuario elija la ubicación de la carpeta donde están los archivos SIF. Luego:

- Busca todos los archivos con extensión .sif.

- Convierte cada archivo a formato .txt y .asc.

- Guarda los archivos convertidos en una subcarpeta llamada TXT_Convertidos y ASC_Convertidos.

- Muestra en consola el progreso y posibles errores durante la conversión.

## Cómo usarlo

1. Descarga y ejecuta el script en tu terminal o entorno Python:

```bash
python sif2txtascii.py
```

2. Se abrirá una ventana para seleccionar la carpeta que contiene los archivos .sif.

3. El script realizará la conversión y guardará los archivos .txt y .asc en las carpetas TXT_Convertidos y ASC_Convertidos dentro de la carpeta seleccionada.

## Contacto

Para dudas o sugerencias, puedes abrir un issue en este repositorio.

## Licencia

Este proyecto está bajo licencia MIT. Puedes usarlo y modificarlo libremente siempre que incluyas el aviso de derechos de autor incluido en LICENSE en todas las copias o porciones sustanciales del Software.
