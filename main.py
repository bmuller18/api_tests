import requests


def ShowNames():
    for a in data:
            print(a['name'])

# URL correcta de la API
url = "https://api.thedogapi.com/v1/breeds"

try:
    # Realizando la solicitud GET
    response = requests.get(url)

    # Verificando que la solicitud fue exitosa (código 200)
    if response.status_code == 200:
        # Convertir la respuesta en formato JSON
        data = response.json()
        ShowNames()
    else:
        print(f"Error en la solicitud: {response.status_code}")

except requests.exceptions.RequestException as e:
    # Manejar posibles errores de la solicitud
    print(f"Ha ocurrido un error: {e}")




