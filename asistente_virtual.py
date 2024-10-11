import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
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
    return engine.runAndWait()

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
        momento = 'Buenos días'
    else:
        momento = 'Buenas tardes'

    # Decir el saludo
    hablar(f'Hola {momento}, soy Sabina, tu asistente personal. Por favor dime en que te puedo ayudar')

# Funcion central del asistente
def pedir_cosas():

    #Activar saludo inicial
    saludo_inicial()

    # Variable de corte 
    comenzar = True

    while comenzar:

        # Activar el micro y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('Con gusto estoy abriendo YouTube.')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar('Claro estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('Buscando eso en Wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar('Wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('ya mismo estoy en eso')
            pedido = pedido.replace('busca en internet', '')
            pywhatkit.search(pedido)
            hablar('Esto es lo que ehe encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea ya lo estoy reproduciendo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'chiste' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {
                'apple': 'APPL',
                'amazon': 'AMZN',
                'google': 'GOOGL'
            }
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontré, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('No la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar('Me voy a descansar, cualquier cosa me avisas')
            break


pedir_cosas()


