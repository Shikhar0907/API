import requests
import urllib

def book():
    URL = "https://www.booknomads.com/api/v0/isbn/"
    param = str(input("Please enter the ISBIN: "))
    URL = URL + param
    data = requests.get(URL)
    js = data.json()
    for d in js['Authors']:
        print(d['Name'])


def main():
    book()



main()
