# Asistente de Voz
Este es un asistente de voz desarrollado en Python que permite realizar diferentes tareas como abrir páginas web, informar la fecha y la hora, y ejecutar otros comandos mediante reconocimiento de voz.

## Requisitos
Antes de ejecutar este proyecto, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.10+
- pip (el gestor de paquetes de Python)
- Librerías de Python:
    - pyttsx3
    - speech_recognition
    - pywhatkit
    - yfinance
    - pyjokes
    - webbrowser
    - wikipedia

## Instalación
1. Clona este repositorio:
    ```bash 
    git clone https://github.com/alonso1298/Asistente-de-Voz.git
    cd Asistente-de-Voz
2. Crea un entorno virtual (opcional, pero recomendado):
    ```bash 
    python -m venv env
3. Activa el entorno virtual:
- En Windows:
    ```bash 
    .\env\Scripts\activate
- En MacOS/Linux:
    ```bash 
    source env/bin/activate
4. Instala las dependencias:
    ```bash 
    pip install -r requirements.txt
    ```
    Si no tienes un archivo requirements.txt, puedes crear uno con las dependencias mencionadas arriba:
    ```bash 
    pip install pyttsx3 speech_recognition pywhatkit yfinance pyjokes wikipedia
    pip freeze > requirements.txt
    ```
5. Instala PyAudio:

    PyAudio es necesario para el reconocimiento de voz y puede requerir una instalación específica:
- En Windows:
    ```bash 
    pip install pipwin
    pipwin install pyaudio
- En MacOS/Linux:
    ```bash 
    pip install pyaudio
## Uso
1. Ejecuta el script principal:
    ```bash 
    python asistente_virtual.py
2. Interacción con el asistente:

    El asistente de voz estará listo para escuchar tus comandos de voz. Puedes hacer preguntas como:
    - "Abrir YouTube"
    - "Qué día es hoy"
    - "Qué hora es"
    - "Abrir navegador"

## Personalización
Puedes ajustar la voz del asistente modificando las opciones de voz en el código:
``` python
# Opciones de voz / idioma
    id1 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'  # Español
    id2 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'   # Inglés
```
## Contribuciones

Las contribuciones son bienvenidas. Si deseas contribuir, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (git checkout -b feature/nueva-funcionalidad).
3. Realiza los cambios y haz commit (git commit -m 'Agrega nueva funcionalidad'). 
4. Sube tu rama (git push origin feature/nueva-funcionalidad).
5. Abre un Pull Request.






