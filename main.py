from controller.dao import VueloDAO
import speech_recognition as sr

vuelo_dao = VueloDAO()


def hablar():
    reconocedor = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ajustando el ruido ambiental...")
        reconocedor.adjust_for_ambient_noise(source)
        print("Escuchando...")
        audio = reconocedor.listen(source)
        try:
            audio = reconocedor.listen(source, timeout=3, phrase_time_limit=10)
            print("Reconociendo...")
            texto = reconocedor.recognize_google(audio, language="es-ES")
            print("Texto reconocido: " + texto)
            return texto
        except sr.UnknownValueError:
            print("No se pudo entender el audio")
            return None
        except sr.WaitTimeoutError:
            print("Tiempo de espera agotado")
            return None
        except sr.RequestError as e:
            print(f"No se pudo solicitar resultados; {e}")
            return None
        except Exception as e:
            print(f"Error inesperado: {e}")
            return None

def agregar_vuelo():
    print("Ingrese el código del vuelo:")
    codigo = hablar()
    if codigo is None:
        print("No se pudo reconocer el código del vuelo")
        return
    print("Ingrese la aerolínea:")
    aerolinea = hablar()
    if aerolinea is None:
        print("No se pudo reconocer la aerolínea")
        return
    print("Ingrese el destino:")
    destino = hablar()
    if destino is None:
        print("No se pudo reconocer el destino")
        return
    print("Ingrese el tipo de vuelo (Regular/Emergencia):")
    tipo = hablar()
    if tipo is None:
        print("No se pudo reconocer el tipo de vuelo")
        return
    
    if tipo == "Emergencia":
        vuelo_final= vuelo_dao.agregar_primero(codigo, aerolinea, destino, tipo)
    else:
        vuelo_final= vuelo_dao.agregar_vuelo(codigo, aerolinea, destino, tipo)
    
    if not vuelo_final:
        print("El vuelo ya existe")
        return
    print("Vuelo agregado exitosamente")
    menu()

def ver_vuelo():
    vuelo = vuelo_dao.ver_primero()
    if vuelo:
        print(f"Vuelo: {vuelo.codigo}, Aerolínea: {vuelo.aerolinea}, Destino: {vuelo.destino}, Tipo: {vuelo.tipo}")
    else:
        print("No hay vuelos disponibles")
    menu()
def eliminar_vuelo():
    vuelo_dao.quitar_vuelo()
    print("Vuelo eliminado exitosamente")

def menu():
    print("1.   Agregar vuelo")
    print("2.   Ver vuelo")
    print("3.   Eliminar vuelo")
    print("4.   Salir")
    seleccion = hablar()
    seleccion = seleccion.lower() if seleccion else None
    if not seleccion:
        print("No se pudo reconocer la opción")
    if seleccion == "agregar vuelo":
        agregar_vuelo()
    elif seleccion == "ver vuelo":
        ver_vuelo()
    elif seleccion == "eliminar vuelo":
        eliminar_vuelo()
    elif seleccion == "salir":
        print("Saliendo...")
        exit()
    else:
        print("Opción no válida")
        menu()
menu()