import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pywhatkit
import pyjokes
import webbrowser
import datetime
import wikipedia

# Opciones de voz / idioma 
id1 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

# Escuchar nuesto microfono y devolver el audio como texto 
def transformar_audio_en_texto():

    # Almacenar el recognizer en una cariable 
    r = sr.Recognizer()

    # Configurar el microfono
    with sr.Microphone() as origen:

        # Ajustar para el ruido de fondo
        r.adjust_for_ambient_noise(origen)  

        # Tiempo de espera 
        r.pause_threshold = 0.8

        # informar que comenzo la grabación 
        print('Ya puedes hablar')

        # Guardar lo que escuche como audio 
        audio =  r.listen(origen)

        try:
            # Buscar en google 
            pedido = r.recognize_google(audio, language="es-mx")

            # Prueba de que pudo ingresar 
            print("Dijiste: " + pedido)

            # Devolver a pedido
            return pedido
        
        # En caso de que no comprenda el audio
        except sr.UnknownValueError:

            #Pueba de que no comprendio el audio
            print('ups, no entendio')

            # Devolver error
            return 'Sigo esperando'
        
        # En caso de que no pudo resolver el pedido 
        except sr.RequestError:

            #Pueba de que no comprendio el audio
            print('No hay servicio')

            # Devolver error
            return 'Sigo esperando'
        
        # Error inseperado 
        except:

            #Pueba de que no comprendio el audio
            print('Ups, algo ah salido mal')

            # Devolver error
            return 'Sigo esperando'
        
#Función para que el asistente pueda ser escuchado 
def hablar(mensaje):

    # Enceder el motor de pyttsx3
    engine = pyttsx3.init()

    # Se configura la voz 
    engine.setProperty('voice', id1)

    # pronuncia el mesaje
    engine.say(mensaje)
    # Se encarga de que diga y ejecute el mensaje
    engine.runAndWait()

# Informar el dia de la semana
def pedir_dia():

    # Variable con datos del dia actual
    dia = datetime.date.today()
    print(dia)

    # Crear una variable para el dia de la semana 
    dia_semana = dia.weekday()
    print(dia_semana)

    #diccionario con nombres de los dias 
    calendario = {
        0: 'Lunes', 
        1: 'Martes',
        2: 'Miércoles',
        3: 'Jueves',
        4: 'Viernes',
        5: 'Sábado',
        6: 'Domingo',
        }
    
    # Decir dia de la semana 
    hablar(f'Hoy es {calendario[dia_semana]}')


# Informar la hora
def pedir_hora():

    # Variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    print(hora)

    # Decir la Hora
    hablar(hora)

# Función saludo inicial
def saludo_inicial():

    # Crear variable con datos de hora 
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento = 'Buenos dias'
    else:
        momento = 'Buenas tardes'

    # Decir el saludo
    hablar(f'Hola {momento}, soy Sabina, tu asistente personal. Por favor dime en que te puedo ayudar')

saludo_inicial()

