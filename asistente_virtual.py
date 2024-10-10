import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance
import pywhatkit
import pyjokes
import webbrowser
import datetime
import wikipedia

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



id1 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'
id2 = r'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'


hablar('Hola Alonso. espero que tengas un buen dia')