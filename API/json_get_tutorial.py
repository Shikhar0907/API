import requests
import json

def json_test():
    URL = 'https://reqres.in'
    URL = URL + '/api/users?'
    param = {'page':2}
    req = requests.get(URL,params = param)
    print(json.dumps(req.json(),indent=4))

def json_post():
    URL = 'https://reqres.in'
    URL = URL + '/api/users'
    payload = {"name": "morpheus","job": "leader"}
    request = requests.post(URL,data=payload)
    print(request.json())
    


def main():
    #json_test()
    json_post()


main()
