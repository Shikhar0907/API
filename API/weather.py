import requests

def weather():
    URL = "https://samples.openweathermap.org/data/2.5/weather?"
    city_id = str(input("Please enter the city id: "))
    key = 'b6907d289e10d714a6e88b30761fae22'
    param = {'id' : city_id, 'appid' : key}
    data = requests.get(url = URL, params = param).json()
    for keys, values in data['main'].items():
        print(keys,values)



def main():
    weather()

main()
