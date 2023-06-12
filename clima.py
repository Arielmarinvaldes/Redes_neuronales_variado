import requests

# city = input("De que ciudad quieres conocer el clima: ")
# url = f"https://es.wttr.in/{city}"

# res = requests.get(url)
# print(res.text)

def return_weather(city):
    url = f"https://es.wttr.in/{city}?format=j1"
    
    response = requests.get(url)
    weather_dic = response.json()

    temp_c = weather_dic["current_condition"][0]['temp_C']
    desc_temp = weather_dic["current_condition"][0]['lang_es']
    desc_temp = desc_temp[0]['value']
    return temp_c, desc_temp

def clima():
    city = input("Enter a city: ")
    temp_c, desc_temp = return_weather(city)
    print(f"La temperatura actual de {city} es {temp_c} °C. {desc_temp}.")

    
if __name__ == '__main__':
    clima()