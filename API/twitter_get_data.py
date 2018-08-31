import requests

def get_data():
    URL = 'https://api.twitter.com/1.1/statuses/show.json?'
    data = '210462857140252672'
    req = requests.get(URL,params = data).json()
    print(req)


def main():
    get_data()

main()
