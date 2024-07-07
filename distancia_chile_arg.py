import requests

def calcular_distancia_duracion(ciudad_origen, ciudad_destino, medio_transporte, api_key):
    url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={ciudad_origen}&destinations={ciudad_destino}&key={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción si la solicitud no fue exitosa

        data = response.json()

        if data["status"] == "OK":
            distancia_texto = data["rows"][0]["elements"][0]["distance"]["text"]
            distancia_valor = data["rows"][0]["elements"][0]["distance"]["value"] / 1000.0
            duracion = data["rows"][0]["elements"][0]["duration"]["text"]

            print(f"Distancia: {distancia_texto} ({distancia_valor:.2f} km)")
            print(f"Duracion del viaje: {duracion}")

            print(f"\nViajando desde {ciudad_origen} a {ciudad_destino} en {medio_transporte}, llegarás a tu destino en {duracion}. ¡Buen viaje!")

        else:
            print(f"No se pudo obtener la información de la distancia y duración del viaje. Mensaje de error: {data['error_message']}")

    except requests.exceptions.HTTPError as http_err:
        print(f"Error HTTP al hacer la solicitud: {http_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Error durante la solicitud: {req_err}")
    except Exception as err:
        print(f"Ocurrió un error inesperado: {err}")

def main():
    print("Bienvenido al calculador de distancia y duración de viaje.")
    api_key = "AIzaSyDoH5hKLvW5TETklYX7KjbtCZ-xFLE20Vo"  # Reemplaza con tu clave de API válida de Google Maps
    while True:
        ciudad_origen = input("Ingrese la ciudad de origen en español: ")
        ciudad_destino = input("Ingrese la ciudad de destino en español: ")
        medio_transporte = input("Elija el tipo de medio de transporte (ej. avion, auto, tren, etc.): ")

        calcular_distancia_duracion(ciudad_origen, ciudad_destino, medio_transporte, api_key)

        salir = input("¿Desea salir del programa? (Ingrese 's' para salir): ")
        if salir.lower() == 's':
            print("Gracias por usar nuestro servicio. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()
