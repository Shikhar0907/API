import requests 

def dreamfactory():
    data = requests.get("https://github.com/Coinigy/api/blob/master/coinigy_ws_config.json").json()
    for d in data:
        print(d)



def main():
    dreamfactory()


main()
