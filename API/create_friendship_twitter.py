import requests

def google_api():
    url = "http://maps.googleapis.com/maps/api/geocode/json"
    locations = "Cambridge School Noida"
    param = {'address':locations}
    data = requests.get(url = url,params=param)
    j = data.json()
    print(j['results'][0]['geometry']['location']['lat'])

    

def main():
    google_api()


main()
