# Tarea1
Tarea 1 de Juan Isidro Martínez Cavazos
Comandos para ejecutar la imagen

Para construir la imagen, use el siguiente comando:

docker build -t calculadora .
Este comando creará una imagen de Docker llamada calculadora.

Para ejecutar la imagen, use el siguiente comando:

docker run -p 8000:8000 calculadora
Este comando creará un contenedor que ejecutará la aplicación en el puerto 8000.

Explicación de los comandos

FROM python:3.9

Este comando especifica la imagen de Docker base que se utilizará para crear la imagen. En este caso, se utilizará la imagen de Python 3.9.

La imagen de Python 3.9 incluye el intérprete de Python 3.9, así como una serie de bibliotecas básicas de Python.

WORKDIR /app

Este comando establece el directorio de trabajo predeterminado para los comandos siguientes.

El directorio de trabajo predeterminado es el directorio /. Sin embargo, es una buena práctica establecer un directorio de trabajo específico para cada aplicación.

En este caso, estableceremos el directorio de trabajo en /app. Esto nos permitirá copiar los archivos de la aplicación en este directorio.

COPY requirements.txt .

Este comando copia el archivo requirements.txt al directorio de trabajo.

El archivo requirements.txt contiene una lista de las dependencias de la aplicación.

Cuando se ejecuta el comando pip install -r requirements.txt, se instalarán estas dependencias.

COPY app.py .

Este comando copia el archivo app.py al directorio de trabajo.

El archivo app.py contiene el código de la aplicación.

RUN pip install --upgrade pip

Este comando actualiza la versión de pip.

pip es una herramienta que se utiliza para instalar paquetes Python. Es importante mantener pip actualizado para garantizar que se instalen las últimas versiones de los paquetes.

RUN pip install -r requirements.txt

Este comando instala las dependencias especificadas en el archivo requirements.txt.

Como se mencionó anteriormente, el archivo requirements.txt contiene una lista de las dependencias de la aplicación.

Este comando instalará estas dependencias en el contenedor.

CMD ["python", "app.py"]

Este comando especifica el comando que se ejecutará cuando se inicie el contenedor.

En este caso, se ejecutará el archivo app.py.
