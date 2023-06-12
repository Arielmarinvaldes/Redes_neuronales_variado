# import requests
# import urllib

# api_url = "https://www.mapquestapi.com/directions/v2/route?"
# key = "gjf0lv1rsogl9qOiSoSpzkHVqUBTLcnn"


# while True:
#     origin = input("ingresa el origen: ")
#     if origin == 's':
#         break
#     destination = input("ingresa el destino: ")
#     if destination == 's':
#         break
    
#     url = api_url + urllib.parse.urlencode({"key":key, "from":origin, "to":destination})
#     json_data = requests.get(url).json()
    
#     status_code = json_data["info"]["statuscode"]
#     if status_code == 0:
#         trip_duration = json_data["route"]["formattedTime"]
#         distance = json_data["route"]["distance"] * 1.61
#         print("=======================================")
#         print(f"Informacion del vieje desde {origin.capitalize()} hasta {destination.capitalize()}.")
#         print(F"Duracion del vieje {trip_duration}")
#         print("distancia: " + str("{:.2f}".format(distance) + "Km"))
#         print("=======================================")
#         print("indicaciones")

#         for each in json_data["route"]["legs"][0]["maneuvers"]:
#             distance_remaining = distance - each["distance"] * 1.61
#             print(each["narrative"] + " (" + str("{:.2f}".format(distance_remaining)) + " Km faltances)")
#             distance = distance_remaining




import requests
import urllib
import geocoder

api_url = "https://www.mapquestapi.com/directions/v2/route?"
key = "gjf0lv1rsogl9qOiSoSpzkHVqUBTLcnn"

while True:
    origin = input("Ingresa el origen (o presiona Enter para utilizar la ubicación actual): ")
    if origin == '':
        # Obtener la ubicación actual del usuario
        g = geocoder.ip('me')
        if not g.latlng:
            print("No se pudo determinar la ubicación actual.")
            continue
        origin = f"{g.latlng[0]},{g.latlng[1]}"
    elif origin.lower() == 's':
        break

    destination = input("Ingresa el destino: ")
    if destination.lower() == 's':
        break
    
    url = api_url + urllib.parse.urlencode({"key": key, "from": origin, "to": destination})
    json_data = requests.get(url).json()
    
    status_code = json_data["info"]["statuscode"]
    if status_code == 0:
        trip_duration = json_data["route"]["formattedTime"]
        distance = json_data["route"]["distance"] * 1.61
        print("=======================================")
        print(f"Información del viaje desde {origin.capitalize()} hasta {destination.capitalize()}.")
        print(F"Duración del viaje: {trip_duration}")
        print("Distancia: " + str("{:.2f}".format(distance) + " Km"))
        print("=======================================")
        print("Indicaciones:")

        for each in json_data["route"]["legs"][0]["maneuvers"]:
            distance_remaining = distance - each["distance"] * 1.61
            print(each["narrative"] + " (" + str("{:.2f}".format(distance_remaining)) + " Km faltantes)")
            distance = distance_remaining
