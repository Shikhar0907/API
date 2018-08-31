import requests
import json

def hackthis_form_data():
    URL = 'https://www.hackthis.co.uk/?login'
    data = {'username':'USERNAME','password':'PASSWORD'}
    req = requests.post(URL,data = data)
    print(req.text)

def main():
    hackthis_form_data()

main()
    
